from wmpy_util.time_util import timer
import datetime
import numpy as np

# ---------------- Console 打印作图 --------------
blank = [chr(183)]  ##此处为空格格式;Windows控制台下可改为chr(12288) ;linux系统中可改为chr(32)【chr(32)==' ' ;chr(183)=='·' ;chr(12288)=='　'】
blank = [chr(12288)]
blank = [chr(32)]
tabs = ['']


class TreeNode:
    __all_dict__ = dict()
    count = 0

    def __new__(cls, id, *args, **kwargs):
        """
        实现基于id的单例
        :param id: 此处id不一定要是数字可以为字符串
        :param args:
        :param kwargs:
        :return:
        """
        if id in TreeNode.__all_dict__:
            return TreeNode.__all_dict__[id]
        else:
            obj = super(TreeNode, cls).__new__(cls)
            obj.id = id
            obj.children = []
            obj.father = None
            obj.number_id = TreeNode.count
            TreeNode.count += 1
            TreeNode.__all_dict__[id] = obj
            return obj

    def __init__(self, id):
        """
        树节点类，继承该类可以轻松实现树状图的绘制
        需要手动往children list中插入节点
        或者调用set_parent设置父节点，可以自动实现关联
        重写__str__方法，以便打印节点的详情
        :param id 节点的唯一id
        """
        pass

    def get_children(self):
        """
        获得所有子节点
        :return:
        """
        return self.children

    def get_parent(self):
        """
        获得父节点
        :return:
        """
        return self.father

    def set_father_by_id(self, fid):
        """
        通过id设置父节点
        :param fid:
        :return:
        """
        f_node = TreeNode.get_node_by_id(fid)
        f_node.add_child(self)

    def __set_father(self, father):
        """

        :param father:
        :return:
        """
        if self.father is not None and not self.father == father:
            raise ValueError("TreeNode cannot have two diff fathers f1=%s  f2=%s" % (str(self.father), str(father)))
        else:
            self.father = father

    def add_child(self, child):
        """
        添加一个子节点
        :param child:
        :return:
        """
        if child not in self.children:
            self.children.append(child)
            child.__set_father(self)

    def add_child_by_id(self, cid):
        """
        通过id设置子节点
        :param cid:
        :return:
        """
        child = TreeNode.get_node_by_id(cid)
        self.add_child(child)

    @staticmethod
    def get_node_by_id(tid):
        """
        通过唯一id获得树节点，如果id不存在则返回null
        :param tid:
        :return:
        """
        if tid in TreeNode.__all_dict__:
            node = TreeNode.__all_dict__[tid]
        else:
            node = None
        return node

    def get_tree_structure(self):
        """
        得到指定的树形结构表示
        :return:
        """
        _result = list()
        _info = str(self)
        _children = self.get_children()
        # 限制描述文字的最大长度为20
        if len(_info) > 20:
            _info = _info[0:10] + "..."
        _result.append(_info)
        if _children is not None and len(_children) > 0:
            _child_infos = list()
            for child in _children:
                _child_infos += child.get_tree_structure()
            _result.append(_child_infos)
        return _result

    def plot_tree(self):
        """
        绘制树形图
        :return:
        """
        print("-" * 20)
        structure = self.get_tree_structure()
        # print(structure)
        print("-" * 5)
        plot_tree(structure)

    def plot_tree2(self, tab=""):
        """
        绘制树形图方法2, better!
        :return:
        """
        size = 2
        child_len = len(self.children)
        s = '─' * size
        if child_len > 0:
            s += '┬'
        else:
            s += '─'
        s += '─' * size
        print(s, end="")
        print(str(self))
        tab = tab + blank[0] * size
        for index, child in enumerate(self.children):
            # 最后一个子节点特殊处理
            if index + 1 == child_len:
                pre = '└'
            else:
                pre = '├'
            print(tab + pre, end="")
            if index + 1 == child_len:
                tab += blank[0]
            else:
                tab += '│'
            child.plot_tree2(tab=tab)
            tab = tab[:-1]

    def delete(self):
        """
        删除该节点
        :return:
        """
        if self.id in TreeNode.__all_dict__:
            TreeNode.__all_dict__.pop(self.id)

    def __str__(self):
        return str(self.id)


def plot_tree(lst):
    lst_len = len(lst)
    if lst_len == 0:
        print('─' * 3)
    else:
        for i, j in enumerate(lst):
            if i != 0:
                print(tabs[0], end='')
            if lst_len == 1:
                s = '─' * 3
            elif i == 0:
                s = '┬' + '─' * 2
            elif i + 1 == lst_len:
                s = '└' + '─' * 2
            else:
                s = '├' + '─' * 2
            print(s, end='')
            if isinstance(j, list) or isinstance(j, tuple):
                if i + 1 == lst_len:
                    tabs[0] += blank[0] * 3
                else:
                    tabs[0] += '│' + blank[0] * 2
                plot_tree(j)
            else:
                print(j)
    tabs[0] = tabs[0][:-3]


def exp_plot_tree():
    """
    测试画树形图
    :return:
    """
    Linux = 'Fedora', ['Debian', ['Ubuntu', ['Kubuntu', 'Xubuntu', 'Edubuntu']], ['KNOPPIX']], [
        ['Puppy Linux']], 'Open SUSE', 'Gentoo', 'Slackware', ['abc', 'def']
    Android = 'Android 1.5 Cupcake', 'Android 1.6  Donut ', 'Android 2.2/2.2 Froyo', 'Android 2.3 Gingerbread', \
              'Android 3.0 Honeycomb', 'Android 4.0 Ice Cream Sandwich'
    OS = [['Unix', [['Free BSD', 'Mac OS']], [Linux]], ['Dos', ['MS-DOS']], 'Windows'], \
         [], ['iOS', Android, 'Symbian', 'BlackBerry OS', 'WebOS', []]
    print('OS')
    plot_tree(Linux)


if __name__ == '__main__':
    exp_plot_tree()
