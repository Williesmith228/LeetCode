# !/usr/local/bin/python3
# -*- coding:utf-8 -*-
#***************************************#
# Author:        zilong.wu@aispeech.com
# Created:       2020-06-08 13:05:49
# Last modified: 2020-06-08 13:05:49
# Filename:      66_plus_one.py
# Copyright      © Aispeech
#***************************************#

def plusOne(digits):
    sum = 0
    for index, v in enumerate(digits):
        sum += v * 10 ** (len(digits) - 1 - index)
    sumPlusOne = sum + 1
    strPlusOne = str(sumPlusOne)
    plusOneArray = []
    lenStrPlusOne = len(strPlusOne)
    tmp = sumPlusOne 
    for i in range(lenStrPlusOne):
        b = lenStrPlusOne - 1 - i
        div = tmp//(10 ** b)
        mod = tmp % (10 ** b)
        tmp = mod
        plusOneArray.append(div)
    return plusOneArray

print(plusOne([1,2,3,4]))
