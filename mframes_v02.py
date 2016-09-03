#!/Users/hanswillemgijzel/anaconda/bin/python

"""returns the missing frames from a folder with one or more image sequences"""

# command line application install instructions Mac OSX:
#
# 1. Put a shebang at the top of the script e.g. #!/usr/local/bin/python. type 'which python' in terminal if you don't know what the shebang should be.
# 2. Save the file without '.py' extension, open terminal and type 'chmod u+x <filename>', to make the file executable.
# 3. Copy the file to one of the PATH folders. To find PATH, type $PATH in terminal (returns multiple folders separated by ':').
#
# How to use: open terminal, and type:
# $ mframes <path/to/folder/with/image/sequence/>

import sys
import os
import re

def main():

    # get the number in a filename
    def getNumber(f):
        return re.findall('\d+', os.path.splitext(f)[0])[-1]


    # get the extension of a filename
    def getExtension(f):
        return os.path.splitext(f)[1]


    # get the path from the user
    if len(sys.argv) < 2:
        print 'no path!'
        sys.exit(0)
    else:
        p = sys.argv[1]

    fileNames = [f for f in os.listdir(p) if f[0] != '.']
    
    try:
        checkForNumbers = [getNumber(f) for f in fileNames]
    except:
        print 'please remove files without numbers in the filename!'
        sys.exit(0)

    # get the different image sequences
    sequences = []
    extensions = []
    for f in fileNames:
        fnumber = getNumber(f)
        ext = getExtension(f)
        currentSequence = f[: -1 * (4 + len(fnumber))]
        if currentSequence not in sequences:
            sequences.append(currentSequence)
            extensions.append(ext)


    # put the filenumbers in differen lists
    sequencesFiles = []
    for i in range(len(sequences)):
        newSeq = [int(getNumber(f)) for f in fileNames if f[: -1 * (4 + len(getNumber(f)))] == sequences[i]]
        sequencesFiles.append(newSeq)


    # get missing frames per sequence
    missingFrames = []
    index = 0
    for seq in sequencesFiles:
        start = seq[0]
        end = seq[-1]
        for i in range(start, end + 1):
            if i not in seq:
                print str(sequences[index]) + str(i) + str(extensions[index]) + ' is missing'
                missingFrames.append(i)
        index += 1

    if len(missingFrames) == 0:
        print 'no missing frames!'


if __name__ == '__main__':
    main()
