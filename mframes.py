#!/Users/hanswillemgijzel/anaconda/bin/python

"""returns the missing frames from an image sequence"""

# command line application install instructions Mac OSX:
# 
# 1. Put a shebang at the top of the script e.g. #!/usr/local/bin/python. type 'which python' in terminal if you don't know what the shebang should be.
# 2. Save the file without '.py' extension, open terminal and type 'chmod u+x <filename>', to make the file executable.
# 3. Copy the file to one of the PATH folders. To find PATH, type $PATH in terminal (returns multiple folders separated by ':').
#
# In terminal:
# mframes <path/to/folder/with/image/sequence/>


import sys
import os
import re

def main():
    if len(sys.argv) < 2:
        print 'no path!'
    else:
        p = sys.argv[1]

        try:
            # get numbers from filenames and excluding hidden files
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
