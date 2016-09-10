#!/Users/hanswillemgijzel/anaconda/bin/python

# pgif
#
# Converts an image sequence into a gif.
# It assumes that the framerate of image sequence should be interpreted as 60 fps
# It outputs a gif at 30 fps.
#
# Dependencies: ffmpeg (https://ffmpeg.org/)
#
# command line application install instructions Mac OSX:
#
# 1. Put the correct shebang at the top of the script e.g. #!/usr/local/bin/python. type 'which python' in terminal if you don't know what the shebang should be.
# 2. Save the file without '.py' extension, open terminal and type 'chmod u+x <filename>', to make the file executable.
# 3. Copy the file to one of the PATH folders. To find PATH, type 'echo $PATH' in terminal (returns multiple folders separated by ':').
#
# Usage:
# $ pgif <path/to/folder/with/image/sequence/>

import os
import sys
import re

def getNumber(f):
    return re.findall('\d+', os.path.splitext(f)[0])[-1]

def getAllFilesInFolder(p):
    return [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f)) and f[0] != '.']

os.chdir(sys.argv[1])
fullPath = os.getcwd()
allFiles = getAllFilesInFolder(fullPath)
startNumber = getNumber(allFiles[0])
firstFile, ext = os.path.splitext(allFiles[0])
firstFileFormatted = firstFile[:-len(startNumber)] + '%' + str(len(startNumber)) + 'd' + ext

ffmpegCommand = 'ffmpeg -start_number ' + startNumber + ' -r 60 -i ' + firstFileFormatted + ' -r 30 output.gif'
os.system(ffmpegCommand)
