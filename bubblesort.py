def bubbleSort(l):     
    for i in range(len(l)):
        for j in range(len(l) - 1):
            a = l[j]
            b = l[j + 1]
            if a > b:
                l[j] = b
                l[j + 1] = a
    return l
