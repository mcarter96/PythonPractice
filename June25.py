# June 25
# Given two integers, write a function to sum the numbers without using any arithmetic operators.
# Problem source: https://www.byte-by-byte.com/sum/

def sum(num1, num2):
    if num2 == 0:
        return num1
    
    total = num1 ^ num2
    carry = num1 & num2

    if carry == 0:
        return total
    else:
        return sum(total, carry << 1)

numA = 8
numB = 3
print(sum(numA, numB))