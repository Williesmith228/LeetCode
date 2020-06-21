# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-06 14:17:23
# Last modified: 2020-06-06 14:17:23
# Filename:      35_search_insert.py
# Copyright      © Aispeech
#***************************************#
# the most normal solution
def searchInsert(nums, target):
    lenNums = len(nums)
    for i in range(0, lenNums - 1):
        if target == nums[i]:
            return i
        else:
            if target > nums[i] and target < nums[i+1]:
                return i+1
    if target == nums[lenNums-1]:
        return lenNums - 1
    elif target > nums[lenNums-1]:
        return lenNums
    elif target < nums[0]:
        return 0

print(searchInsert([1,3,5,6],2))

def searchInsertOptimize(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        print('left', left, 'right', right, 'mid', mid, nums[mid], target)
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return left
print(searchInsertOptimize([1,2,5,6], 2))
