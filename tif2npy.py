# -*- coding: utf-8 -*-
from skimage import io as skimage_io 
import numpy as np
import h5py
import warnings


file_name = '../data/gridrec70-740/rec_' # without tif extension
max_tif_index = 670


# read stack of tiffs
for m in range(max_tif_index):
    if m < 10:
        fname = file_name + '0000' + str(int(m)) + '.tif'
    elif m < 100:
        fname = file_name + '000' + str(int(m)) + '.tif'
    elif m < 1000:
        fname = file_name + '00' + str(int(m)) + '.tif'
    else:
        fname = file_name + '0' + str(int(m)) + '.tif'
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        out = skimage_io.imread(fname, plugin='tifffile')
    
    if m == 0:
        sx = max_tif_index
        sy, sz = out.shape
        data = np.zeros((sx, sy, sz), dtype='float32')

    data[m, :, :] = out
    print fname


# write data
np.save('../data/gridrec70-740/gridrec70-740.npy', data)