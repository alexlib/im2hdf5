# -*- coding: utf-8 -*-

#____________single_tiff_to_numpy_array__________________##

# from __future__ import division
# import tomopy
# import os
# from numpy import *
# import matplotlib.pyplot as mpl
#
# data_dir = '/Volumes/Socha_MP8/Mosquito_tomo/raw_tiff'
#
# output_dir = '/Volumes/Socha_MP8/Mosquito_tomo/arrays'
# outfile = 'wdarkdata.npy'
# # the directory to look into
# file = 's40_2011_08_Aedes4_00001_dark_01504.tif'
# filename = os.path.join(data_dir, file)
# outfilename = os.path.join(output_dir, outfile)
#
# # Open file in read-only mode.
# I = mpl.imread(filename)
# save(outfilename, I)

##______________tiff_stack_to_numpy_array____________________##

from __future__ import division
import tomopy
import os
import numpy as np
import matplotlib.pyplot as mpl

data_dir = '/Volumes/Socha_MP8/Mosquito_tomo/raw_tiff/'
file_0 = 's40_2011_08_Aedes4_00001_00002.tif'
filename_0 = os.path.join(data_dir, file_0)

output_dir = '/Volumes/Socha_MP8/Mosquito_tomo/arrays/'
outfile = 'data.npy'
outfilename = os.path.join(output_dir, outfile)

file_base = 's40_2011_08_Aedes4_00001_'
# Open file in read-only mode.
I = mpl.imread(filename_0)
I_saved = np.save(outfilename, I)

for i in range(2,1504):
    if i < 10:
        file_x = file_base + '0000' + str(i) +'.tif' 
        filename_x = os.path.join(data_dir, file_x)
    elif i < 100:
        file_x = file_base + '000' + str(i) +'.tif' 
        filename_x = os.path.join(data_dir, file_x)
    elif i < 1000:
        file_x = file_base + '00' + str(i) +'.tif' 
        filename_x = os.path.join(data_dir, file_x)    
    else:
        file_x = file_base + '0' + str(i) +'.tif' 
        filename_x = os.path.join(data_dir, file_x)
    print (i)
    # Open file in read-only mode.
    N = mpl.imread(filename_x)
    I = np.load(outfilename)
    args = [I,N]
    I =+ np.dstack(args)
    I_saved = np.save(outfilename, I)
    
# the directory to look into

#np.save(outfilename, I)


