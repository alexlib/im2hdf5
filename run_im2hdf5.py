from im2hdf5 import *

# Directory containing the TIF images to be converted to HDF.
# The white field, dark-field, and scan images need to be in this folder.
inputDir = '/Users/matthewgiarra/Desktop/im2hdf5/data'

# Image extension
imageExt='tif'

# Starting row (slice) in the scan
scanStartRow = 0

# Ending row (slice) in the scan
# "None" will use all the rows (slices) starting with the "starting row" from above
scanEndRow = None

# Base name of the scan images (everything before the numbers, i.e., "image" for "image_000001.tif")
# Replace "none" with the base names of the images.
dataBase='proj_'

# Base name of the white field images.
whiteBase='proj_'

# Base name of the dark field images
darkBase='proj_'

# Starting image number for the scan images.
dataStart = 132

# Ending image number for the scan images.
# "None" will use all the images beginning with the "starting image" from above
dataEnd = 140

# Starting image number for the white field images.
# "None" will start at the first image with the matching base name, I think.
whiteStart = 61

# Ending image number for the white field images.
# "None" will use all the images beginning with the "starting image" from above
whiteEnd = 61

# Starting image number for the dark field images.
darkStart = 60

# Ending image number for the dark field images.
darkEnd = 60

# Class of the images
dataClass = 'uint8'

# Directory in which to save the outputs
outputDir='./hdf'

# Name of the output file
outputFileName = 'out.h5'

# Number of digits in the file names
numDig = 6

# Run the data conversion code.
convert_images(inputDir = inputDir, imageExt=imageExt, scanStartRow = scanStartRow, scanEndRow = scanEndRow, dataBase=dataBase, whiteBase=whiteBase, darkBase=darkBase, dataStart=dataStart, dataEnd=dataEnd,  whiteStart=whiteStart, whiteEnd=whiteEnd, darkStart=darkStart, darkEnd=darkEnd, dataClass = dataClass, outputDir=outputDir, outputFileName = outputFileName, numDig = numDig)