# binary search (k = search keyword, l = sorted list)
def search(k, l):
    l_search = msort(l)
    while True:
        mid = int(len(l_search) / 2)
        if k < l_search[mid]:
            l_search = l_search[:mid]
        elif k > l_search[mid]:
            l_search = l_search[mid:]
        else:
            return True
        if len(l_search) < 1:
            return False
