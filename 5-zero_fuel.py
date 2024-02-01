# WPU Coding Challenge 2024 But in Python
# 5/366
# https://www.codewars.com/kata/5861d28f124b35723e00005e

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump/mpg <= fuel_left

print(zero_fuel(100, 50, 1))