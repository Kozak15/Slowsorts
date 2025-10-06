import random
def slowsort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

def recur_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        m = max(lst)
        lst.remove(m)
        return recur_sort(lst)+[m]

def issorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def bogo_sort(lst):
    while not issorted(lst):
        random.shuffle(lst)
    return lst
l = [ random.randint(0,100) for _ in range(10) ]
print("Unsorted list:", l)
sorted_l = slowsort(l)
print("Sorted list:", sorted_l)