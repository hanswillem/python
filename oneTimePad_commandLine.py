#!/PUT/THE/RIGHT/SHEBANG/HERE!

# One Time Pad Command Line Application
# Can be used to encrypt and decrypt txt files
#
# command line application install instructions Mac OSX:
#
# 1. Put the correct shebang at the top of the script e.g. #!/usr/local/bin/python. type 'which python' in terminal if you don't know what the shebang should be.
# 2. Save the file without '.py' extension, open terminal and type 'chmod u+x <filename>', to make the file executable.
# 3. Copy the file to one of the PATH folders. To find PATH, type 'echo $PATH' in terminal (returns multiple folders separated by ':').
#
# Encrypt txt file:
# $ otp -e <path/to/file.txt>
#
# Decrypt txt file (key.txt should be in same folder as txt file):
# $ otp -d <path/to/file.txt>

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
    cypherFile = os.path.splitext(messageFile)[0] + '_cypher.txt'

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

    messageFile = cypherFile[:cypherFile.index('_cypher.txt')] + '.txt'

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
