#open terminal and type 'python mframes.py ' followed by the path to the file

import sys
import os
import re

def main():
    p = sys.argv[1]

    #get numbers from filenames and excluding hidden files
    frames = [int(re.findall('\d+', os.path.splitext(f)[0])[-1]) for f in os.listdir(p) if f[0] != '.']


    start = frames[0]
    end = frames[-1]
    print 'missing frames:'
    for i in range(start, end + 1):
        if i not in frames:
            print str(i)



if __name__ == '__main__':
    main()
