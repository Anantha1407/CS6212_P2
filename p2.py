import time
start = time.time_ns()
def median_of_medians(array, k):
    if len(array) <= 5:
        array.sort()
        return array[k]
    #Divide given array into small groups of size(5 typically)
    groups = [array[i:i+5] for i in range(0, len(array), 5)]
    medians = [median_of_medians(group, len(group) // 2) for group in groups]
    #Finding the pivot
    pivot = median_of_medians(medians, len(medians) // 2)
    #Partitioning the list into sublists
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    if k < len(left):
        return median_of_medians(left, k)
    elif k < len(left) + len(middle):
        return pivot
    else:
        return median_of_medians(right, k - len(left) - len(middle))
import random
#Generate 10000 random numbers between 1 and 10000000
randomlist = random.sample(range(1, 10000000),10000)
k = len(randomlist)//2
print("Expected Result:", median_of_medians(randomlist, k))
end = time.time_ns()
print(end - start)
