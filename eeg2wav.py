#!/Users/hanswillemgijzel/anaconda/bin/python

"""converts eeg data in .txt format to a .wav file"""

# Command line application install instructions Mac OSX:
#
# 1. Put the correct shebang at the top of the script e.g. #!/usr/local/bin/python. type 'which python' in terminal if you don't know what the shebang should be.
# 2. Save the file without '.py' extension, open terminal and type 'chmod u+x <filename>', to make the file executable.
# 3. Copy the file to one of the PATH folders. To find PATH, type 'echo $PATH' in terminal (returns multiple folders separated by ':').
#
# how to use:
#
# In terminal type 'eeg2wav' + SPACE + filename of the .txt file, and press enter.
# The .wav file will have the same name as the .txt file, and will be put in the same folder.


import sys
import os
import wave
import struct


def main():

    #scale the array
    def scaleArray(a):
        temp_a = []

        for i in a:
            temp_a.append(abs(i))

        mx = max(temp_a)

        for i in range(len(a)):
            a[i] /= mx
            a[i] *= 32767  #the maximum amplitude for a 16 bit wave file (2**16 = 65536, so a range from -32767 to +32767)
            a[i] *= -1 #invert it
            a[i] = int(a[i])

        return a


    #read the eeg, put it in an array and scale it with the function above
    def readEeg(txtFile):
        global scaledEeg
        f = open(txtFile, 'r')
        eeg_input = []
        i = 0;

        for n in f:
            n = n.strip()
            n = float(n)
            n = int(n)
            eeg_input.append(n)

        scaledEeg = scaleArray(eeg_input)

        f.close()


    #make the waveform
    def makeWavetable(waveFile):
        wv = wave.open(waveFile, 'w')
        wv.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

        for i in range(len(scaledEeg)):
                value = scaledEeg[i]
                packed_value = struct.pack('h', value)
                wv.writeframes(packed_value)
                wv.writeframes(packed_value) #there are 2 chanels, so the value needs to be written 2 times

        wv.close()


    #get the filename and set the .wav filename
    fname = sys.argv[1]
    wvname = fname[0:-3] + 'wav'

    #read and convert the data
    readEeg(fname)
    makeWavetable(wvname)
    print('>> finished!')



if __name__ == '__main__':
    main()
