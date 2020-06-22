# June 17
# Given an array of integers where each value 1 <= xx <= len(array), write a function that finds all the duplicats in the array
# Problem source: https://www.byte-by-byte.com/findduplicates/

def dups(arr):
    arr.sort()
    duplicates = []

    for x in range(len(arr)-1):
        if arr[x] == arr[x+1]:
            duplicates.append(arr[x])
    
    return duplicates

print(dups([1, 2, 3]))
print(dups([1, 2, 2]))
print(dups([3, 3, 3]))
print(dups([2, 1, 2, 1]))