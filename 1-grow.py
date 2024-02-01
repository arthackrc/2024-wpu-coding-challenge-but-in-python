# WPU Coding Challenge 2024 But in Python
# 1/366
#https://www.codewars.com/kata/57f780909f7e8e3183000078

""" def grow(arr):
    result = 1
    for array in arr:
        result *= array
    return result """

from functools import reduce
def grow(arr):
    return reduce(lambda acc, curr: acc * curr, arr)
    
print(grow([1,2,3,4]))