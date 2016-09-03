#!/Users/hanswillemgijzel/anaconda/bin/python

"""returns the missing frames from an image sequnce"""

import sys
import os
import re

def main():
    if len(sys.argv) < 2:
        print 'no path!'
    else:
        p = sys.argv[1]

        try:
            #get numbers from filenames and excluding hidden files
            frames = [int(re.findall('\d+', os.path.splitext(f)[0])[-1]) for f in os.listdir(p) if f[0] != '.']
            missingFrames = []

        except:
            print 'that does not seem to be a folder with an image sequence!'
            sys.exit(0)

        start = frames[0]
        end = frames[-1]

        for i in range(start, end + 1):
            if i not in frames:
                print str(i)
                missingFrames.append(i)

        if len(missingFrames) == 0:
            print 'no missing frames!'



if __name__ == '__main__':
    main()

