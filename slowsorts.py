import random
#O(n**2) time
def slowsort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
#O(n**2) time
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
#O(n*n!) time
def bogosort(lst):
    while not issorted(lst):
        random.shuffle(lst)
    return lst
#O(n log n)?
def radix_sort_binary(lst):
    length = len(lst[0])
    loop_counter = 0
    counter = -2
    ans = []
    temp_0 = []
    temp_1 = []
    for item in lst:
        if item[-1] == '0':
            temp_0.append(item)
        elif item[-1] == '1':
            temp_1.append(item)
    ans = temp_0 + temp_1
    while loop_counter < length - 1:
        ans_0 = []
        ans_1 = []
        for item in ans:
            if item[counter] == '0':
                ans_0.append(item)
            elif item[counter] == '1':
                ans_1.append(item)
        ans = ans_0 + ans_1
        counter -= 1
        loop_counter += 1
    return ans
def radix_sort_denary(lst):
    mx_len = 0
    lst_a = []
    for item in lst:
        mx_len = max(mx_len , len(str(item)))
    for item in lst:
        lst_a.append('0' * (mx_len - len(str(item))) + str(item))
    loop_counter = 0
    counter = -1
    while loop_counter < mx_len:
        ans_0,ans_1,ans_2,ans_3,ans_4,ans_5,ans_6,ans_7,ans_8,ans_9 = [],[],[],[],[],[],[],[],[],[]
        for item in lst_a:
            if item[counter] == '0':
                ans_0.append(item)
            elif item[counter] == '1':
                ans_1.append(item)
            elif item[counter] == '2':
                ans_2.append(item)
            elif item[counter] == '3':
                ans_3.append(item)
            elif item[counter] == '4':
                ans_4.append(item)
            elif item[counter] == '5':
                ans_5.append(item)
            elif item[counter] == '6':
                ans_6.append(item)
            elif item[counter] == '7':
                ans_7.append(item)
            elif item[counter] == '8':
                ans_8.append(item)
            elif item[counter] == '9':
                ans_9.append(item)
        counter -= 1
        loop_counter += 1
        lst_a = ans_0 + ans_1 + ans_2 + ans_3 + ans_4 + ans_5 + ans_6 + ans_7 + ans_8 + ans_9
    
    lst_final = []
    for item in lst_a:
        while item[0] == '0':
            item = item[1:]
        lst_final.append(item)
    lst_final_final = []
    for item in lst_final:
        lst_final_final.append(int(item))
    return lst_final_final

def radix_sort_den(lst):
    l1 = [ bin(item)[2:] for item in lst]
    l2 = radix_sort_binary(l1)
    l3 = [int(item,2) for item in l2]
    return l3



l = [ random.randint(0,100) for _ in range(10) ]


