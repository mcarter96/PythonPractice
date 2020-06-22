# June 15
# Given a list of items with values and weights, as well as a max weight, find the maximum value you can generate from items where the sum of the weights is less than the max.
# Problem source: https://www.byte-by-byte.com/01knapsack/

def knapsack(value, weight, maxWeight, items):

    # If the max weight has been reached or there are no more items
    if items == 0 or maxWeight == 0:
        return 0
    
    else:
        # if the last item is more than the max weight, skip that item
        if weight[items-1] > maxWeight:
            return knapsack(value, weight, maxWeight, items-1)
        
        # if the item is less than the max weight, then you want to see what the larger value is between the last item and not adding the item
        else: 
            return max(value[items-1] + knapsack(value, weight, maxWeight-weight[items-1], items-1), knapsack(value, weight, maxWeight, items-1) )


# How the matrix is set up for the following solution
# For each spot, you want to look at the spot above the one you're filling to get that weight (knap[a-1][b]). Then compare that to the element one row up and the maxWeight at that spot minus the weight value (knap[a-1][b-weight[a-1]]) 
# then add the previous value (value[a-1])
# e.g. for filling spot knap[3][4], you will look at the max between knap[2][4], which is 16, and value[2] and knap[2][4-3], which is 12 and 6. Since 12 and 6 is 18, that's greater than 16 so that's what fills knap[3][4]
# value = [6, 10, 12]
# weight = [1, 2, 3]
# maxWeight = 5
#   0  1  2  3  4  5 
# 0 0  0  0  0  0  0
# 1 0  6  6  6  6  6
# 2 0  6  10 16 16 16
# 3 0  6  10 16 18 22



def knapsackMatrix(value, weight, maxWeight, items):
    # initalize the matrix for the weight in the knapsack
    knap = [[0 for x in range(maxWeight+1)] for y in range(items+1)]

    # for each element in the array, calculate what the max value would be of the item added
    for a in range(items+1):
        for b in range(maxWeight+1):
            if a == 0 or maxWeight == 0:
                knap[a][b] = 0
            # put the max of either the value of the item being added or the 
            elif weight[a-1] <= b:
                knap[a][b] = max(value[a-1] + knap[a-1][b-weight[a-1]], knap[a-1][b])
            else:
                knap[a][b] = knap[a-1][b]
    
    # return the bottom right element in the table, which is the maximum value
    return knap[items][maxWeight]





value = [6, 10, 12]
weight = [1, 2, 3]
maxWeight = 5
items = len(value)
print(knapsack(value, weight, maxWeight, items))
print(knapsackMatrix(value, weight, maxWeight, items))