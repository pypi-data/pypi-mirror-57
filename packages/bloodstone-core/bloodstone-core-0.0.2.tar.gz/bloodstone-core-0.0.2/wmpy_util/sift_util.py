#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WeiWang Zhang
@Time    : 2019-09-20 12:09
@File    : sift_util.py
@Software: PyCharm
@Desc    : TODO:describtion here
"""
from wmpy_util.time_util import timer
from wmpy_util import img_util as iu
from wmpy_util import file_util as fu
import numpy as np
import cv2
import time

sift = cv2.xfeatures2d.SIFT_create()
MIN_MATCH_COUNT = 10
KNN_MATCH_SUPPRESS = 0.8  # KNN匹配的极大值抑制比例，该值越小则符合要求的匹配越少


class LocateCard:
    def __init__(self):
        pass

    @timer
    def locate(self, img, template, template_feature=None, xfeature_img_width=600, mask_func=None, debug=False):
        """
        寻找图像中的身份证并进行图像矫正（透视变换）
        :param img:  为需要识别的图像
        :param template: 模板图片
        :param template_feature: 模板特征，可以为空，为空则重新计算
        :param xfeature_img_width: 计算特征时的宽度尺寸
        :param mask_func: 需要识别的图像的特征mask计算函数，接收图片返回mask
        :param debug:
        :return:
        """
        # if len(img.shape) == 3:
        #     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # trainImage in Gray
        # else:
        #     img_gray = img
        # img_scale为放大缩小倍数的倒数（逆变换所需要除以的系数）
        img_small, img_scale = iu.img_resize_longer_size(img, xfeature_img_width)
        img_mask = None
        if callable(mask_func):
            img_mask = mask_func(img_small)
        # 计算sift计算中的模板尺寸
        h_temp, w_temp = template.shape[0:2]
        # 目标图片缩小的倍数
        #  scale定义为变换后/变换前  ratio定义为变换前/变换后
        img_ratio = 1 / img_scale
        # 模板图片缩小倍数
        template_ratio = w_temp / xfeature_img_width
        kp1, kp2, match = self.findMatchWithXFeature(img_small, mask=img_mask, template=template,
                                                     template_feature=template_feature)
        # reshape为(x,y)数组
        src_pts = np.float32([kp1[m.queryIdx].pt for m in match]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in match]).reshape(-1, 1, 2)
        # 逆缩放变换，得到两张大图之间的点对应关系
        src_pts = src_pts * template_ratio  # 模板上的点
        dst_pts = dst_pts * img_ratio  # 对应目标图片上的点
        # 用HomoGraphy计算图像与图像之间映射关系, M为转换矩阵
        mat_tr, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        # 计算模板在目标图片上的轮廓
        templ_edge = np.float32([[0, 0], [0, h_temp - 1], [w_temp - 1, h_temp - 1], [w_temp - 1, 0]]).reshape(-1, 1, 2)
        templ_edge_on_img = cv2.perspectiveTransform(templ_edge, mat_tr)
        deskwing_start = time.time()
        # 根据模板尺寸和需求宽度，计算所需图片整体尺寸
        mat_tr = np.mat(mat_tr).I
        im_r = cv2.warpPerspective(img, mat_tr, (w_temp, h_temp), borderValue=[255, 255, 255],
                                   borderMode=cv2.BORDER_REPLICATE)
        # iu.time_spend(deskwing_start, "deskewing")
        # -----------存储中间图片，正式环境不需要------------
        if debug:
            # 存储图片特征mask
            if img_mask is not None:
                iu.save_result(img_mask, fu.get_temp_path("mid_result"), "sift_mask.jpg")
            # 存储原图
            iu.save_result(img, fu.get_temp_path("mid_result"), "origin.jpg")
            img_up = self.get_match_pic(iu.img_resize(template, xfeature_img_width), kp1, img_small, kp2,
                                        matches=match)  # 组合图的上面两张，反应sift匹配情况
            cv2.polylines(img_small, [np.int32(templ_edge_on_img * img_scale)], True, [0, 255, 0], 2,
                          cv2.LINE_AA)  # 画出识别到的卡片边框
            img_below = iu.img_joint_with_colorgap((img_small, iu.img_resize(im_r, xfeature_img_width)),
                                                   axis=1, align=0, gap=2,
                                                   gap_color=[255, 0, 0])  # 组合图的下面两张，分别为带识别框的原图/变换后的图片
            img_sift_combine = iu.img_joint_with_colorgap((img_up, img_below), axis=0, gap=2, gap_color=[255, 0, 0])
            # 画出sift全过程图片
            iu.save_result(img_sift_combine, fu.get_temp_path("mid_result"), "sift_combine.jpg")
        # -----------对结果做出检查，如果离谱则报错，不返回结果------------
        if len(src_pts) <= MIN_MATCH_COUNT:
            print("Error: 模板匹配度不足 - %d/%d" % (len(src_pts), MIN_MATCH_COUNT))
            raise ValueError("Template not found!")
        # TODO计算原图上圈出的身份证面积，并以此判断是否是一个有效的识别（比如面积占比必须大于1/8）
        self.check_area_size(img.shape, templ_edge_on_img)
        # im_r图像矫正结果  M_r对应的透视变换矩阵
        return im_r, mat_tr

    @timer
    def findMatchWithXFeature(self, target, mask=None, template=None, template_feature=None):
        """
        检测两张图片的相似程度，并找到目标图片中的模板位置
        :param target: 目标图片（灰度图像）
        :return:
        """
        global sift
        sift_start = time.time()
        # template_umat = cv2.UMat(template)
        # target_umat = cv2.UMat(target)
        if template_feature is None:
            kp1, des1 = template_feature
        else:
            kp1, des1 = sift.detectAndCompute(template, None)
        kp2, des2 = sift.detectAndCompute(target, mask=mask)
        # iu.time_spend(sift_start, "detect")
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=10)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)
        # store all the good matches as per Lowe's ratio test.
        # FIXME 这个地方不理解了，为什么m需要小于n的0.7
        # 两个最佳匹配之间距离需要大于ratio 0.7,距离过于相似可能是噪声点
        good = []
        for m, n in matches:
            if m.distance < KNN_MATCH_SUPPRESS * n.distance:
                good.append(m)
        # 返回依次为，模板特征点，目标图片特征点，匹配情况
        return kp1, kp2, good


    # def find_math_with_scale(self, target, s_target, template, s_template, ):



    def find_match(self, target_feature, template_feature):
        """
        检测两张图片的相似程度，并找到目标图片中的模板位置
        :param target_feature:
        :param template_feature:
        :return:
        """
        kp1, des1 = template_feature
        kp2, des2 = target_feature
        flann_index_kdtree = 0
        index_params = dict(algorithm=flann_index_kdtree, trees=5)
        search_params = dict(checks=10)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        # 寻找模板到目标图片的匹配
        matches = flann.knnMatch(des1, des2, k=2)
        # store all the good matches as per Lowe's ratio test.
        # FIXME 这个地方不理解了，为什么m需要小于n的0.7
        # 两个最佳匹配之间距离需要大于ratio 0.7,距离过于相似可能是噪声点
        good = []
        for m, n in matches:
            if m.distance < KNN_MATCH_SUPPRESS * n.distance:
                good.append(m)
        # 返回依次为，模板特征点，目标图片特征点，匹配情况
        return kp1, kp2, good

    def showimg(self, img):
        cv2.namedWindow("contours", 0)
        # cv2.resizeWindow("contours", 1600, 1200);
        cv2.imshow("contours", img)
        cv2.waitKey()

    def check_area_size(self, shape, dst):
        """
        检测识别到的卡片区域是否有效
        :param shape: 图片尺寸 [h,w]
        :param dst:  标记身份证区域的多边形顶点
        :return:
        """
        # 计算原图面积
        ori_area = shape[0] * shape[1]
        card_area = cv2.contourArea(dst)
        # 如果识别到的卡片面积过大或者过小则不予判断
        if card_area < (ori_area / 8) or card_area > (ori_area * 1.5):
            raise ValueError(" 识别到的卡片面积异常 识别/实际 = %.2f" % (card_area / ori_area))
        max_cor = np.max(dst, axis=0)
        min_cor = np.min(dst, axis=0)
        [[width, height]] = max_cor - min_cor
        # 如果识别到的卡片高宽过大或者过小则不予判断
        if width < (shape[1] / 4) or width > (shape[1] * 1.5):
            raise ValueError("识别到的卡片宽度异常 识别/实际 = %.2f" % (width / shape[1]))
        if height < (shape[0] / 5) or height > (shape[0] * 1.5):
            raise ValueError("识别到的卡片高度异常 识别/实际 = %.2f" % (height / shape[0]))

    def get_match_pic(self, tmpl, templ_kp, target, target_kp, matches):
        """
        获得sift匹配状态连线图，用于测试
        :param tmpl: 模板图片
        :param templ_kp: 模板特征点
        :param target: 目标图片
        :param target_kp: 目标图片特征点
        :param matches: 特征点匹配情况
        :return:
        """
        img = cv2.drawMatches(tmpl, templ_kp, target, target_kp, matches, outImg=None,
                              flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
        return img


locate_card = LocateCard()
