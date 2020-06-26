# June 26
# Given a stack, reverse the items without creating any additional data structures.
# Problem source: https://www.byte-by-byte.com/reversestack/

def reverse(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    tempArr = []
    arrLength = len(arr)-1
    while arrLength > -1:
        tempArr.append(arr[arrLength])
        arrLength = arrLength - 1
    
    return tempArr


arr1 = [1, 2, 3]
arr2 = [5, 7, 3, 29]
print(reverse(arr1))
print(reverse(arr2))