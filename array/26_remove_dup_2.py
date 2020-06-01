# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-02 07:31:02
# Last modified: 2020-06-02 07:31:02
# Filename:      26_remove_dup_2.py
# Copyright      © Aispeech
#***************************************#

def removeDup(nums):
    lenNums = len(nums)
    if lenNums in [0,1]:
        return lenNums
    for i in range(lenNums-1,0,-1):
        if nums[i] == nums[i-1]:
            del nums[i]
    return len(nums)

print(removeDup([1,1,1,2,2,2,3,3,4,5,6]))
