# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-18 16:32:02
# Last modified: 2020-06-18 16:32:02
# Filename:      169_major_element.py
# Copyright      © Aispeech
#***************************************#

def majorityElementBest(nums):
    """
        @param: nums, list
        @return: int
    """
    return sorted(nums)[len(nums)//2]



def majorityElement(nums):
    major_count = len(nums)//2
    count_dict = {}
    for j, v in enumerate(nums):
        if v in count_dict:
            tmp = count_dict[v] + 1
        else:
            count_dict[v] = 1
        if count_dict[v] > major_count:
            return v
