# WPU Coding Challenge 2024 But in Python
# 3/366
# https://www.codewars.com/kata/59ca8246d751df55cc00014c

""" def hero(bullets, dragons):
    if bullets / 2 >= dragons:
        return True
    else:
        return False """

def hero(bullets, dragons):
    return bullets / 2 >= dragons
    
print(hero(10,15))