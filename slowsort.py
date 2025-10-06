import random
def slowsort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
l = [ random.randint(0,100) for _ in range(10) ]
print("Unsorted list:", l)
sorted_l = slowsort(l)
print("Sorted list:", sorted_l)