# June 10
# Implement a priority queue
# Problem souce: https://www.byte-by-byte.com/priorityqueue/

import heapq
from queue import PriorityQueue

# Not a practically implementation since it needs to be sorted after each addition.
# o(n log n) to maintain the order
def simplePriority():
    cars = []
    cars.append((4, "Toyota")) # no sorting after this since one item
    cars.append((2, "Chevrolet"))
    cars.sort() # sort after each item is added to keep correct order
    cars.append((3, "Subaru"))
    cars.sort()
    cars.append((1, "Tesla"))
    cars.sort()

    while cars:
        print(cars.pop(0))

# Uses the heapq module from Python
# o(log n) to inserting elements 
def heapPriority():
    cars = []
    heapq.heappush(cars, (3, "BMW"))
    heapq.heappush(cars, (2, "Audi"))
    heapq.heappush(cars, (4, "Volkswagon"))
    heapq.heappush(cars, (1, "Porsche"))

    while cars:
        print(heapq.heappop(cars))

# Uses the priorityqueue class
# o(log n)
def queuePriority():
    cars = PriorityQueue()

    cars.put((3, "GMC"))
    cars.put((2, "Chrysler"))
    cars.put((4, "Ford"))
    cars.put((1, "Pergot"))

    while not cars.empty():
        print(cars.get())

queuePriority()