# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-02 06:55:12
# Last modified: 2020-06-02 06:55:12
# Filename:      26_remove_dup.py
# Copyright      © Aispeech
#***************************************#

def removeDup(nums):
    lenNums = len(nums)
    if lenNums in [0, 1]: # 如果数组长度只有0或者1，则直接返回长度，因为已经不重复了
        return lenNums
    final_index = 1
    for i in range(1, lenNums): # range 从1开始比较方便
        if nums[i] != nums[i-1]: # 如果当前位置元素的值 不等于 它前面元素的值，则将当前位置的值复制给 不重复索引 的位置：final_index
                                  # 且将不重复索引 final_index 加1
            nums[final_index] = nums[i]
            final_index += 1
    return final_index

print(removeDup([1,1,1,2,2,2,3,3,4,5,6]))



