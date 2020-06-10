import array
import math

# June 9
# Find the median of two sorted arrays.

def median(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    arrLength = len(arr1)
    if arrLength % 2 == 0:
        medianValue = int(math.floor(arrLength/2))
        value1 = arr1[int(math.floor(arrLength/2))]
        value2 = arr1[int(math.floor(arrLength/2)-1)]
        median = (value1 + value2) / 2
    else:
        median = arr1[int(math.floor(arrLength/2))]
    return median

def testMedian():
    arrA = [1, 3, 5]
    arrB = [2, 4, 6]
    print (median(arrA, arrB))

