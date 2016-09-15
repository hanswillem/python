def sortList(l):
    ls = []
    while len(l) > 0:
        record = 0
        for i in l:
            if i > record:
                record = i
        ls.append(record)
        l.pop(l.index(record))

    return ls
