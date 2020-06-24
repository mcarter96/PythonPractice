# June 19
# Given a list of packages that need to be built and the dependencies for each package, determine a valid order in which to build the packages.
# Problem source: https://www.byte-by-byte.com/buildorder/

# Packages with dependecies
# 0: 
# 1: 0
# 2: 0
# 3: 1, 2
# 4: 3
# Valid build order: 0, 1, 2, 3, 4
# Alt valid buidl: 0, 2, 1, 3, 4

def buildOrder(processes):
    tempMark = set()
    permMark = set()
    result = set()

    for x in range(len(processes)):
        if x not in permMark:
            visit(x, tempMark, permMark, result, processes)
    
    return result

def visit(currProcess, tempMark, permMark, result, processes):

    if currProcess in tempMark:
        print("Error")
    
    if currProcess not in permMark:
        tempMark.add(currProcess)
        for x in processes[currProcess]:
            visit(x, tempMark, permMark, result, processes)
        permMark.add(currProcess)
        tempMark.remove(currProcess)
        result.add(currProcess)

packages = [[], [0], [0], [1, 2], [3]]
print(buildOrder(packages))
