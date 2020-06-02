# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-03 06:58:30
# Last modified: 2020-06-03 06:58:30
# Filename:      27_remove_element.py
# Copyright      © Aispeech
#***************************************#
def removeEle(nums, val):
    """
        @param: nums, list
        @param: val, int
    """
    lenNums = len(nums)
    index = 0
    for i in range(0, lenNums): # 索引从0开始，因为可能第一个元素就和val相等
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

nums = [1,2,3,3,3,2,3,3,5]
ind = removeEle(nums, 3)
i = 0
while i < ind:
    print(nums[i])
    i += 1

