#binary search (expects a sorted list)
def search(k, l):
    l_search = msort(l)
    while True:
        print l_search
        mid = int(len(l_search) / 2)
        if k < l_search[mid]:
            l_search = l_search[:mid]
        elif k > l_search[mid]:
            l_search = l_search[mid:]
        else:
            return True
