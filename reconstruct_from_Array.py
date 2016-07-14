# -*- coding: utf-8 -*-

# This script is meant to allow a user to call a function in terminal to reconstruct a sample. Saves data as 16-bit images.

from __future__ import division

import tomopy
import os
import matplotlib.pyplot as mpl
import glob
import numpy as np

# This function 
def recon_180(data_dir='.', file = 'out.h5', output_dir='/Volumes/Socha_MP8/', num_proj=1800, z=15, eng=27.4, lens=2, center=None):
    
    ##_________________________inputs_and_parameters_______________________
    
    file_name = os.path.join(data_dir, file)
    output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

    d = tomopy.xtomo_dataset(log='debug')
    
    # Program does not complete a sample if actual number of slices is input. This somewhat arbitrary scaled value seems to work well.
    #num_proj = (3/2)*num_proj
    # These values work well with the computer's available memory and produce quality images.
    chunk_size = 50
    margin_slices = 20

    # Define pixel size from function argument lens. 
    pxl = 0
    if lens == 2:
        pxl = 5.5e-4  #for 2X lens
    elif lens == 5:
        pxl = 2.2e-4  #for 5X lens
    
    rat = 5e-04  
    
    num_chunk = np.int(np.ceil(num_proj / (chunk_size - margin_slices)))
    if num_proj == chunk_size:
        num_chunk = 1

    ##________________________rescale_for_16-bit_image____________________
    # data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=(np.int(num_proj/2)), slices_end=(np.int(num_proj/2))+chunk_size)
    #
    # d = tomopy.xtomo_dataset(log='debug')
    # d.dataset(data, white, dark, theta=theta)
    # d.zinger_removal(zinger_level=500, median_width=5)
    # d.normalize(negvals=1, cutoff=1)
    # #d.stripe_removal()
    # #d.phase_retrieval(alpha=0.005)
    # d.center=center
    #
    # d.gridrec()
    # d.apply_mask(ratio=0.95)
    #
    # data_min = d.data_recon.min()
    # data_max = d.data_recon.max()
    

    

    ##________________________reconstruction______________________________
    #Importing small arrays of data from a saved numpy array.
    data = np.load('/Volumes/Socha_MP8/Mosquito_tomo/arrays/data.npy')
    white = np.load('/Volumes/Socha_MP8/Mosquito_tomo/arrays/whitedata.npy')
    dark = np.load('/Volumes/Socha_MP8/Mosquito_tomo/arrays/darkdata.npy')
    theta = np.load('/Volumes/Socha_MP8/Mosquito_tomo/arrays/data.npy')
    
    
    
    
    

    # Xtomo object creation and pipeline of methods.  
    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta)
    d.normalize()
    d.correct_drift()
    d.phase_retrieval()
    d.correct_drift()
    d.center=661.5
    d.gridrec()
    tomopy.xtomo_writer(output_file, dtype='uint16', axis=0, data_max=None, overwrite = True)
    d.FLAG_THETA = False
    print 'Finished reconstructing slices from ' + file
    
    
    # for ii in xrange(num_chunk):
#         if ii == 0:
#             SliceStart = ii*chunk_size
#             SliceEnd = (ii+1)*chunk_size
#         else:
#             SliceStart = ii*(chunk_size-margin_slices)
#             SliceEnd = SliceStart + chunk_size
#             if SliceEnd > (num_proj):
#                 SliceEnd = num_proj
#
#         data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=SliceStart,slices_end=SliceEnd,white_start=3,white_end=9,dark_start=3,dark_end=9)
#         data[0,:,:] = data[1,:,:]
#         d.dataset(data, white, dark, theta)
#         d.zinger_removal(median_width=15,zinger_level=500)
#         d.normalize()
#         #d.correct_drift(10)
#         d.stripe_removal(wname="sym16",level=10,sigma=4)
#         d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#         d.center = center
#         d.gridrec()
#
#         # Finds center of rotation
#         if center == None:
#             d.optimize_center(ratio=0.8)
#         else:
#             d.center=center
#
#         d.gridrec()
#
#
        #d.apply_mask(ratio=1.1)
       
        #data[0,:,:] = data[1,:,:]
        #d = tomopy.xtomo_dataset(log='debug')
        #d.dataset(data, white, dark, theta)
        ##d.zinger_removal(median_width=15,zinger_level=200)
        #d.normalize()
        ##d.stripe_removal(wname="sym16",level=10,sigma=2)
        ##d.stripe_removal(level=10,sigma=1)
        #d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
        ##d.stripe_removal(wname="sym16",level=10,sigma=4)
        #data_size = d.data.shape
        ##d.median_filter(10)
        ##d.optimize_center(ratio=0.3) 
        ##print d.center
        
    
    
#############################################################################################################
#############################################################################################################

data_dir = '/Volumes/Socha_MP8/Mosquito_tomo'
file = 's40_2011_08_Aedes4.hdf'
output_dir = '/Volumes/Socha_MP8/Mosquito_tomo/reconstructed'
num_proj = 1199
z = 30
eng = 27.4
lens = 5
center = 900
recon_180(data_dir=data_dir, file=file, output_dir=output_dir, num_proj=num_proj, z=z, eng=eng, lens=lens, center=center)
