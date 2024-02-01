# WPU Coding Challenge 2024 But in Python
# 6/366
# https://www.codewars.com/kata/5556282156230d0e5e000089

def dna_to_rna(dna):
    rna = dna.replace("T", "U")
    return rna

print(dna_to_rna("TTTT"))