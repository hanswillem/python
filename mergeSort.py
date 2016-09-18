def merge(l1, l2):
    l_sorted = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            l_sorted.append(l1[0])
            l1.pop(0)
        else:
            l_sorted.append(l2[0])
            l2.pop(0)

    if len(l1) > 0:
        l_sorted += l1
    if len(l2) > 0:
        l_sorted += l2
    return l_sorted

def mergeSort(l):
    l_all = [[i] for i in l]
    l_sorted = []
    
    while True:
        for i in range(0, len(l_all) - 1, 2):
            l_sorted.append(merge(l_all[i], l_all[i + 1]))

        # if there is an item left in l_all (i.e. if the length of l_all was uneven), add it to l_sorted
        if len(l_all) % 2 != 0:
            l_sorted.append(l_all[-1])

        # if there is only 1 item in l_sorted, the sorting is done
        if len(l_sorted) == 1:
            return l_sorted[0]

        l_all = l_sorted
        l_sorted = []


l = [5,3,9,6,1,0,4,3,8]
print mergeSort(l)
