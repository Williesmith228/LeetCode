# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-09 06:50:55
# Last modified: 2020-06-09 06:50:55
# Filename:      88_merge_sorted_array.py
# Copyright      © Aispeech
#***************************************#
def mergeSortedArray(nums1, m, nums2, n):
    nums1[:] = nums1[:m] + nums2 
    return sorted(nums1)

print(mergeSortedArray([1,2,4], 3, [3,8,9], 3))



