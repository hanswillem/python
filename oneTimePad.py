#One Time Pad

m = 'Secret'
k = [0,3,6,1,2,5]


def encrypt(m, k):
    c = []
    for i in range(len(m)):
        c.append((ord(m[i]) + k[i]) % 123)
    return c
    

def decrypt(c, k):
    m = []
    for i in range(len(c)):
        m.append(chr((c[i] - k[i]) % 123))
    return ''.join(m)


print 'M: '+ m
print 'K: ' + str(k)
c = encrypt(m, k)
print 'C: ' + str(c)
print 'D: ' + decrypt(c, k)
