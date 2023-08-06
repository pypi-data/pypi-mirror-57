#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WeiWang Zhang
@Time    : 2019-09-19 14:33
@File    : time_util.py
@Desc    : 时间日期，计时工具等
"""

import time
import datetime
import inspect
from collections import Iterable, Iterator

DATETIME_FORMATER = '%Y-%m-%d %H:%M:%S'
DATE_FORMATER = '%Y-%m-%d'
DATETIME_FORMATER_YmdHM = '%Y-%m-%d %H:%M'
DATETIME_FORMATER_mdHM = '%m-%d %H:%M'
DATETIME_FORMATER_mdH = '%m-%d %Hh'
DATETIME_FORMATER_md = '%m-%d'
DATETIME_FORMATER_dH = '%dd-%Hh'
DATETIME_FORMATER_HM = '%H:%M'
DATETIME_FORMATER_MS = '%M:%S'

FORMAT_LIST = [DATETIME_FORMATER,
               DATE_FORMATER]


def get_timestamp_by_str(date_str, _format=None):
    if _format is not None:
        return time.mktime(time.strptime(date_str, _format))
    time_obj = None
    try:
        time_obj = time.strptime(date_str, DATETIME_FORMATER)
    except ValueError as e:
        pass
    if time_obj is None:
        try:
            time_obj = time.strptime(date_str, DATE_FORMATER)
        except ValueError as e:
            pass
    if time_obj is None:
        return 0
    else:
        return time.mktime(time_obj)


def get_datetime_by_str(date_str, format=DATETIME_FORMATER):
    """

    :param date_str:
    :return:
    """
    if not date_str:
        return None
    _datetime_obj = None
    format_list = FORMAT_LIST
    if format:
        format_list = [format]
    for format in format_list:
        try:
            _datetime_obj = datetime.datetime.strptime(date_str, format)
        except Exception as error:
            # 未能匹配日期格式，不打印错误
            pass
        if _datetime_obj:
            break
    return _datetime_obj


def get_str_by_timestamp(timestamp=None, date_format=DATETIME_FORMATER):
    """
    将时间戳转为指定格式的字符串
    :param timestamp:
    :param format:
    :return:
    """
    if timestamp is None:
        # 如果为空则选取当前时间
        timestamp = time.time()
    time_obj = time.localtime(timestamp)
    return time.strftime(date_format, time_obj)


def get_str_by_datetime(datetime_obj, format=DATETIME_FORMATER):
    """
    将datetime对象转为指定格式的字符串
    :param timestamp:
    :param format:
    :return:
    """
    datetime_str = None
    try:
        datetime_str = datetime.datetime.strftime(datetime_obj, format)
    except Exception as error:
        # 未能匹配日期格式，不打印错误
        pass
    return datetime_str


class FuncTimer:
    """
    用于统计某个函数运行时间的类
    使用@timer注解装饰需要统计时间的函数
    不带参调用方式
    @timer
    def func():
    直接对函数进行统计，并取函数名作为识别名称

    带参调用方式
    @timer(name="test1", combine=True, batch=100)
    def func
    指定函数识别名称为"test1", 并指定统计方式为合并模式，每一百次调用统计一次耗时
    """

    def __init__(self):
        pass

    def timer(self, name="", combine=False, batch=100):
        _name = name

        def decorator(func):
            if _name == "":
                __name = func.__qualname__
            else:
                __name = _name

            def wrapper(*args, **kwargs):
                start = time.time()
                ret = func(*args, **kwargs)
                now = time.time()
                _time_spend = (now - start) * 1000
                if combine:
                    # 如果需要合并结果，则将batch次调用放到一起进行计算和打印
                    add_record(__name, _time_spend, batch)
                else:
                    # 如果不需要合并结果则直接打印函数耗时
                    # logger.info("%s timeUsed = %d ms" % (__name, int(time_spend)))
                    print("%s timeUsed = %d ms" % (__name, int(_time_spend)))
                return ret

            wrapper.__qualname__ = __name
            wrapper.__name__ = __name.split(".")[-1]
            return wrapper

        # 处理未传参数的情况
        if callable(name):
            _func = name
            _name = _func.__qualname__
            decorator = decorator(_func)
        return decorator

    def generator_timer(self, name="", combine=False, batch=100):
        """
        正确处理一个Iterator生成函数的计时问题
        e.g.
        @generator_timer
        def get_generator(x):
            for i in range(x):
                yield x*x

        如果使用@timer注释，只能得到get_generator函数运行时间（只会执行一次）
        使用@generator_timer注释可以得到Iterator每次生产数据所花费的时间
        即，__next__()函数调用花费的时间

        :param name:
        :param combine:
        :param batch:
        :return:
        """
        _name = name

        def decorator(func):
            if _name == "":
                __name = func.__qualname__
            else:
                __name = _name

            def wrapper(*args, **kwargs):
                start = time.time()
                generator = func(*args, **kwargs)
                now = time.time()
                _time_spend = (now - start) * 1000
                print("%s timeUsed = %d ms" % (__name, int(_time_spend)))
                return GeneratorTimer(generator, name=__name, combine=combine, batch=batch)
            wrapper.__qualname__ = __name
            wrapper.__name__ = __name.split(".")[-1]
            return wrapper

        # 处理未传参数的情况
        if callable(name):
            _func = name
            _name = _func.__qualname__
            decorator = decorator(_func)
        return decorator


class GeneratorTimer(Iterator):
    def __init__(self, iterable_obj, name="", combine=False, batch=100):
        """
        对一个迭代器进行包装，并对__next__函数进行计时
        :param iterable_obj:
        :param name:
        :param combine:
        :param batch:
        """
        self.iterable_obj = iterable_obj
        self.name = name
        self.show_name = "{}_generator_data".format(self.name)
        self.combine = combine
        self.batch = batch

    def __iter__(self):
        return self

    def __next__(self):
        start = time.time()
        ret = self.iterable_obj.__next__()
        now = time.time()
        _time_spend = (now - start) * 1000
        if self.combine:
            # 如果需要合并结果，则将batch次调用放到一起进行计算和打印
            add_record(self.show_name, _time_spend, self.batch)
        else:
            # 如果不需要合并结果则直接打印函数耗时
            # logger.info("%s timeUsed = %d ms" % (__name, int(time_spend)))
            print("%s timeUsed = %d ms" % (self.show_name, int(_time_spend)))
        return ret


class SimpleTimer:
    def __init__(self):
        """
        simple timer for code lines
        >> stimer = SimpleTimer()
        >> code 1
        >> code 2
        >> stimer.check("test1")
        >> code 3
        >> stimer.check("test2")
        """
        self._timestamp = time.time()

    def reset(self):
        self._timestamp = time.time()

    def check(self, name):
        _now = time.time()
        _spend = _now - self._timestamp
        self._timestamp = _now
        print("%s timeUsed = %d ms" % (name, int(_spend)))


_time_record = {}


def add_record(name, time_spend, batch):
    """
    TODO 暂时未考虑线程安全的问题
    :param name:
    :param time_spend:
    :param batch:
    :return:
    """
    if name not in _time_record:
        record = dict(sum=0, iter=0)
        _time_record[name] = record
    else:
        record = _time_record[name]
    record["sum"] += time_spend
    record["iter"] += 1
    if record["iter"] == batch:
        _time_sum, _iter = record["sum"], record["iter"]
        _cost_ave = _time_sum / _iter
        print("%s timeSpend %.2f ms on %d iterations, average cost=%.2f" % (name, _time_sum, _iter, _cost_ave))
        _time_record.pop(name)


_func_timer = FuncTimer()
timer = _func_timer.timer
generator_timer = _func_timer.generator_timer


@generator_timer
def fun(x):
    for i in range(x):
        yield i


if __name__ == '__main__':

    gen = fun(10)
    for i in gen:
        print(i)
