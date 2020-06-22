# June 18
# Given an unsorted array, find the length of the longest sequence of consecutive numbers in the array
# Problem source: https://www.byte-by-byte.com/consecutivearray/

def consecutive(consectArr):
    consectArr.sort()
    
    longestArr = []
    tempArr = []
    arrLength = len(consectArr)
    
    for x in range(arrLength-1):
        if x > 0 and consectArr[x] == consectArr[x+1] - 1:
            tempArr.append(consectArr[x+1])
        else:
            tempArr.clear()
            tempArr.append(consectArr[x+1])

        if len(tempArr) > len(longestArr):
            longestArr = tempArr
            tempArr.clear()


    return len(longestArr), longestArr

# Hash solution source: https://www.geeksforgeeks.org/longest-consecutive-subsequence/
def consecutiveHash(conArr):
    aLen = len(conArr)
    arrSet = set()
    ans = 0

    for x in conArr:
        arrSet.add(x)

    for i in range(aLen):
        if (conArr[i]-1) not in arrSet:
            currEle = conArr[i]
            while (currEle in arrSet):
                currEle += 1
            ans = max(ans, currEle-conArr[i])
    
    return ans


arr1 = [4, 2, 1, 6, 5]
arr2 = [5, 5, 3, 1]
arr3 = [6, 3, 2, 4, 7, 5]
print(consecutive(arr2))
print(consecutiveHash(arr2))