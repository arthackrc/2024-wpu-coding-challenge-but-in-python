# WPU Coding Challenge 2024 But in Python
# 8/366
# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

""" def count_sheep(n):
    result = ""
    for i in range(1,n+1):
        result = result + str(i) + " " + "sheep..."
    return(result) """

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

print(count_sheep(4))