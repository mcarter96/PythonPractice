# June 24
# Given an array containing all the numbers from 1 to n except two, find the two missing numbers.
# Problem source: https://www.byte-by-byte.com/twomissingnumbers/

def missing(arr):
    
    missingNum = []
    arr.sort()

    if arr[0] != 1:
        missingNum.append(1)
    for x in range(len(arr)-1):
        if arr[x]+1 != arr[x+1]:
            missingNum.append(arr[x]+1)
    
    if len(missingNum) != 2:
        missingNum.append(arr[-1]+1)
        
    return missingNum


missingArr = [4, 2, 3]
missingArr2 = [4, 2, 1, 6, 3]
missingArr3 = [1, 3]
missingArr4 = [6, 3, 4, 1]
print(missing(missingArr))
print(missing(missingArr2))
print(missing(missingArr3))
print(missing(missingArr4))