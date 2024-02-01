# WPU Coding Challenge 2024 But in Python
# 2/366
# https://www.codewars.com/kata/5a00e05cc374cb34d100000d

""" def reverse_seq(n):
    return [i for i in range(n, 0, -1)] """

def reverse_seq(n):
    return list(range(n, 0, -1))

print(reverse_seq(5))