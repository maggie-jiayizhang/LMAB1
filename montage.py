# LMAB 1 F2021
# Maggie Zhang <jiayizha>

from PIL import Image
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

# assumptions: images: 1104 x 1104
SIZE = 1104
# 5x5 = 25 different fields
ROWS = 5
COLS = 5
FIELDS = ROWS * COLS
# format string: Well + Field + Channel
FORMAT = "%sf%sd%d.TIF"

MAP = [[21, 22, 23, 24, 25],
       [20,  7,  8,  9, 10],
       [19,  6,  1,  2, 11],
       [18,  5,  4,  3, 12],
       [17, 16, 15, 14, 13]]

def build_channel(well, prefix, channel, result):
    for i in range(ROWS):
        for j in range(COLS):
            idx = MAP[i][j] - 1
            if (idx < 10):
                idx = '0'+str(idx)
            filename = well + "/" + prefix + FORMAT%(well, str(idx), channel)
            im_array = np.array(Image.open(filename))
            result[i*SIZE:(i+1)*SIZE, j*SIZE:(j+1)*SIZE] = im_array

def rescale(arr):
    return (arr-arr.min())/(arr.max()-arr.min())

if __name__ == '__main__':
    well = sys.argv[1] # get the directory name we are working on
    entries = os.listdir(well)
    # assumption: all files in the dir has the same prefix
    prefix = "_".join(entries[0].split("_")[:2]) + "_"

    n_ch = 2
    if (len(sys.argv) > 2):
        n_ch = int(sys.argv[2])
    
    # cannot have more than 2 channels
    if (n_ch > 3): assert(0)
    elif (n_ch < 3):
        result_all = np.zeros((ROWS*SIZE, COLS*SIZE))
        build_channel(well, prefix, n_ch, result_all)
        plt.imsave("%sd%d.png"%(well, n_ch), result_all, cmap='gray')
    elif(n_ch == 3):
        channels = [2, 0] # R-PI, G-None, B-Hoechst
        result_all = np.zeros((ROWS*SIZE, COLS*SIZE, 3))
        for channel in channels:
            # enforce that PI gets the first/red channel
            # Hoechst the third/blue channel
            build_channel(well, prefix, channel, result_all[:,:,2-channel]) 
            result_all[:,:,2-channel] = rescale(result_all[:,:,2-channel])
        plt.imsave("%sd%d.png"%(well, n_ch), result_all)

    print("output size: ", np.shape(result_all))

