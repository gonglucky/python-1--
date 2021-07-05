#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/5
# @Author : gongwf
import matplotlib.pyplot as plt
import functools
import random


# 解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 生成随机数组
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


# 函数修饰器
def bounded(num, mininum, maxinum):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            x_axis = random_int_list(mininum, maxinum, num)
            y_axis = random_int_list(mininum, maxinum, num)
            function(x_axis, y_axis)
        return wrapper
    return decorator


# 散点图函数
@bounded(40, 0, 10)
def draw(x_axis, y_axis):
    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(x_axis, y_axis)
    plt.xlabel("X-Axis", fontdict={'size': 16})
    plt.ylabel("Y-Axis", fontdict={'size': 16})
    plt.title("Python 作业4 龚万福-2020103105", fontdict={'size': 20})
    plt.show()


draw()

