# WPU Coding Challenge 2024 But in Python
# 7/366
# https://www.codewars.com/kata/5513795bd3fafb56c200049e

""" def count_by(x, n):
    count =[]
    for i in range(1, n+1):
        times = x * i
        count.append(times)
    return count """

""" def count_by(x, n):
    return [x * i for i in range(1, n + 1)] """

def count_by(x, n):
    return list(range(x, x*n + 1, x))

print(count_by(1, 10))