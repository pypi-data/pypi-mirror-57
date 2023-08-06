#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WeiWang Zhang
@Time    : 2019-11-20 10:57
@File    : data_process.py
@Software: PyCharm
@Desc    : 数据预处理函数
"""
import pandas as pd
from collections import Counter
import random
import os
import sys
from sklearn.base import BaseEstimator, TransformerMixin
from wmpy_util import timer


def _observe_from_data_iter(data_iter, deepth=10, field_map=dict()):
    field_dict = dict()
    for datas in data_iter:
        columns = datas.columns
        for field in columns:
            if field == "id":
                continue
            field_dict.setdefault(field, dict())
            field_series = datas[field]
            if field in field_map:
                map_func = field_map[field]
                field_series = field_series.map(map_func)
            field_counter = Counter(field_series)
            for k, v in field_counter.items():
                field_dict[field].setdefault(k, 0)
                field_dict[field][k] += v
    # 按照字段的稀疏程度进行排序，dense feature排在前面进行显示
    field_dict_sort = sorted(field_dict.items(), key=lambda x: len(x[1]))
    for field, counter in field_dict_sort:
        print("-" * 10, "field: {}".format(field), "-" * 10)
        print("Set size = {}".format(len(counter)))
        _rank = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        print("Most frequency value")
        _num = deepth
        if len(counter) < deepth:
            _num = len(counter)
        for i in range(_num):
            print(_rank[i])
    return field_dict


def _create_data_iter_from_files(files):
    chunksize = 100000
    iter_num = 0
    for file in files:
        if not os.path.isfile(file):
            print("{} is not a file".format(file), file=sys.stderr)
            continue
        data_iter = pd.read_csv(file, chunksize=chunksize)
        try:
            while True:
                data = data_iter.__next__()
                yield data
                iter_num += 1
                if iter_num % 10 == 0:
                    print("{} data processed".format(iter_num * chunksize))
        except StopIteration as error:
            continue


def observe_data_file(data_file, deepth=10, field_map=dict()):
    """
    观察各字段的取值情况
    :param data_file:
    :param deepth: 观察每个字段频率最高的前deepth个取值
    :return:
    """
    data_iter = _create_data_iter_from_files((data_file,))
    return _observe_from_data_iter(data_iter, deepth=deepth, field_map=field_map)


def observe_data_files(data_files, deepth=10, field_map=dict()):
    """
    将多个文件联合统计
    :param data_files:
    :param deepth: 观察每个字段频率最高的前deepth个取值
    :return:
    """
    if not (isinstance(data_files, tuple) or isinstance(data_files, list)):
        raise ValueError("Data files must be a tuple")
    data_iter = _create_data_iter_from_files(data_files)
    return _observe_from_data_iter(data_iter, deepth=deepth, field_map=field_map)


def random_drop_negative(from_file, to_file, field="click", positive=1, negative=0, drop=0.5, seed=100):
    """
    用于处理正负样本不均衡的方式之一
    随机丢弃一部分负样本
    :param from_file: 源文件
    :param to_file: 写入目标文件
    :param field: 标签字段名称
    :param positive: 正样本标签值
    :param negative: 负样本标签值
    :param drop: 丢弃比例
    :param seed: 随机种子
    :return:
    """
    chunksize = 10000
    if not os.path.isfile(from_file):
        print("From_file {} is not a file".format(from_file), file=sys.stderr)
        return
    data_iter = pd.read_csv(from_file, chunksize=chunksize)
    random.seed = seed
    for index, data_frame in enumerate(data_iter):
        flag = data_frame.apply(_random_drop_negative_filter, axis=1, field=field, positive=positive, negative=negative,
                                drop=drop)
        data_frame = data_frame[flag]
        if index == 0:
            header = True
            mode = "w"
        else:
            header = False
            mode = "a"
        data_frame.to_csv(to_file, mode=mode, header=header, index=False, float_format="%.0f")
        if (index + 1) % 10 == 0:
            print("{} data processed".format((index + 1) * chunksize))


def _random_drop_negative_filter(data, *args, field='click', positive=1, negative=0, drop=0.5, **kwargs):
    value = data[field]
    if value == positive:
        # 正例全部保留
        return True
    elif value == negative:
        # 负样本抛弃drop比例的数据
        if random.random() < drop:
            return False
        else:
            return True
    else:
        # 数值在取值范围之外的直接抛弃（只处理二分类问题）
        return False


def form_endless_batch(file_path, func, batch_size=100, cache=False):
    """
    针对大数据集过大而内存有限的情况，无法将所有数据一次性读取到内存当中，所以需要进行分段读取
    该函数通过重复读取文件来产生'无穷无尽'的数据
    同时通过每次跳过随机函数来达到各个epoch之间略微的不同
    :param file_path:
    :param func:
    :param batch_size:
    :return:
    """
    cache_list = []
    # skip_rows = int(random.random() * batch_size)
    data_iter = pd.read_csv(file_path, chunksize=batch_size)
    for data in data_iter:
        gen_data = func(data)
        if cache:
            cache_list.append(gen_data)
        yield gen_data
    while True:
        if cache:
            for gen_data in cache_list:
                yield gen_data
        else:
            data_iter = pd.read_csv(file_path, chunksize=batch_size)
            for data in data_iter:
                yield func(data)


from sklearn.preprocessing import LabelEncoder


class SimpleLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.__class = None
        self.__val_map = None

    @timer
    def fit(self, y):
        self.__class = set(y)
        self.__val_map = {val: index for index, val in enumerate(self.__class)}
        # 未出现的值统一转换为-1
        self.__val_map["None"] = -1

    def transform(self, y):
        if self.__class is None:
            raise ValueError("Encoder not fit yet")
        ret = [self.get_value(val) for val in y]
        return ret

    def get_value(self, y):
        if y in self.__val_map:
            return self.__val_map[y]
        else:
            return self.__val_map["None"]

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X)
        return self.transform(X)





if __name__ == '__main__':
    pass
