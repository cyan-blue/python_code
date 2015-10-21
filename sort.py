#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'yann'

import sys
import datetime
import copy

#MY_LIST = [123,123,12,512,42,21,435,76,98,23,56,878,44,2,1,3,2,5,4,6]
#MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
MY_LIST = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 装饰器是一个以另一个函数为参数的函数
def my_time_decorator(a_function_to_decorate):

    # 在这里，装饰器定义一个函数： 包装器.
    # 这个函数将原始函数进行包装，以达到在原始函数之前、之后执行代码的目的
    def the_wrapper_around_the_original_function(lists):
        begin_time = datetime.datetime.now()
        # 将你要在原始函数之前执行的代码放到这里
        print "Before the function runs", begin_time

        # 调用原始函数(需要带括号)
        a_function_to_decorate(lists)
        end_time = datetime.datetime.now()
        # 将你要在原始函数之后执行的代码放到这里
        print "After the function runs",end_time,"耗时:",(end_time - begin_time).microseconds

    # 代码到这里，函数‘a_function_to_decorate’还没有被执行
    # 我们将返回刚才创建的这个包装函数
    # 这个函数包含原始函数及要执行的附加代码，并且可以被使用
    return the_wrapper_around_the_original_function
@my_time_decorator
def insert_sort(all_list):
    # 插入排序
    lists = copy.copy(all_list)
    print "插入排序-begin",lists,lists is all_list
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            else:
                break
            j -= 1
    print "插入排序-end",lists
    return lists

@my_time_decorator
def shell_sort(all_list):
    # 希尔排序
    lists = copy.copy(all_list)
    print "希尔排序-begin",lists
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    print "希尔排序-end",lists 
    return lists



if __name__=='__main__':
    shell_sort(MY_LIST)
    insert_sort(MY_LIST)



