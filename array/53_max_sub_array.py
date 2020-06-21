# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-07 09:26:08
# Last modified: 2020-06-07 09:26:08
# Filename:      35_max_sub_array.py
# Copyright      © Aispeech
#***************************************#

def maxSubArray(nums):
    maxN=min(nums);sumN=0
    for i in nums:
        if sumN<0:sumN=i
        else:sumN+=i
        if sumN>maxN:maxN=sumN
    return maxN
    
print(maxSubArray([1,2,-1, 3,-1])) 
print(maxSubArray([-1,-3,3,4,-1])) 
