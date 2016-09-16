def sortList(l):
    l_sorted = []
    while len(l) > 0:
        record = l[0]
        for i in l:
            if i < record:
                record = i
        l_sorted.append(record)
        l.pop(l.index(record))
    return l_sorted
