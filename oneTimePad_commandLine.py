#!/PUT/THE/RIGHT/SHEBANG/HERE!

import sys
import os
import random
rnd = random.SystemRandom()

pth = os.path.dirname(sys.argv[2])

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


# encrypt
if sys.argv[1] == '-e':
    m = []

    messageFile = sys.argv[2]
    keyFile = os.path.join(pth, 'key.txt')
    cypherFile = messageFile

    # read message
    f = open(messageFile, 'r')
    for i in f:
        m.append(i.strip())
    f.close()

    m = '\n'.join(m)

    k = [rnd.randint(0, sys.maxint) for i in m]
    c = encrypt(m, k)
    d = decrypt(c, k)


    if m == d:
        print 'Encryption succesful, deleting original message...'
        os.system('srm -v ' + str(messageFile))

        print 'writing cypher and key...'
        # write key
        f = open(keyFile, 'w')
        for i in k:
            f.write(str(i) + '\n')
        f.close()

        # write cypher
        f = open(cypherFile, 'w')
        for i in c:
            f.write(str(i) + '\n')
        f.close()

    else:
        print 'Encryption failed!'


# decrypt
if sys.argv[1] == '-d':

    cypherFile = sys.argv[2]
    keyFile = os.path.join(pth, 'key.txt')

    if not os.path.exists(keyFile):
        print 'key.txt not found in folder!'
        sys.exit(0)

    messageFile = cypherFile

    c = []
    k = []

    # read cypher
    f = open(cypherFile, 'r')
    for i in f:
        c.append(int(i))
    f.close()

    # read key
    f = open(keyFile, 'r')
    for i in f:
        k.append(int(i))
    f.close()

    d = decrypt(c, k)

    print 'Message decrypted, deleting cypher and key...'
    os.system('srm -v ' + cypherFile)
    os.system('srm -v ' + keyFile)

    print 'Writing message...'
    f = open(messageFile, 'w')
    f.write(d)
    f.close()
