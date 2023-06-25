import warnings, subprocess, sys
import numpy as np
import astropy as ap

from astropy.time import Time
from astropy.table import Table
from astropy.timeseries import LombScargle
from astropy.timeseries import TimeSeries
from astropy.io import fits
from scipy.ndimage import rotate
from scipy.special import erf
from astropy.wcs import WCS
from astropy.wcs import utils
from astropy.coordinates import SkyCoord
from astropy import units as u

from astropy.utils.exceptions import AstropyWarning

#import matplotlib.pyplot as plt


# initializing all directories
import os
from os.path import isdir, isfile, join
directory = 'refactor/'	
dir_names = [directory+f+'/' for f in os.listdir(directory) if isdir(join(directory,f))] 


# next thirty lines are from magic_star.py : just iterating through the directories and finding fits files

if __name__ == '__main__':
	
	for d in dir_names:
		image_names = [d+f for f in os.listdir(d) if isdir(join(d,f))]

		# if '00_m_16' in d or 'small_asteroid_lightcurve' in d: continue
		# if not ('HD3' in d or 'VH65' in d or 'XD169' in d or 'XR169' in d or 'CE3' in d or 'CG18' in d or 'CW30' in d or 'EN156' in d or 'JB' in d or 'LT1' in d): continue
		# if not ('EN156' in d or 'EL157' in d or 'FF14' in d or 'GE1' in d) : continue



		start_times = []
		lightcurves = []
		errors      = []

		for f in image_names:
			image_chip_names = [join(f,i) for i in os.listdir(f) if isfile(join(f,i))]
			for ii in image_chip_names: 
				print(ii)

				output_dir_name = f'{ii[:-5]}/'
				# output_dir_name = ii + '/'

				sex_output_name = str(output_dir_name+'sex.cat')

				# print ( output_dir_name )
				print(sex_output_name)

				if not isdir ( output_dir_name ) : os.mkdir ( output_dir_name )

				# os.rename (  )

				temp_output = 'sex_output_temp.dat'

				print(' '.join(['/home/mehul/sextractor/src/sex', ii, '-DETECT_MINAREA', str(150), '-CATALOG_NAME' , sex_output_name  ]))
				print()
				sex = subprocess.run(['/home/mehul/sextractor/src/sex', ii, '-DETECT_MINAREA', str(150), '-CATALOG_NAME' , sex_output_name ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
				fits_file = []

				try:
					fits_file = fits.open ( ii )
				except Exception as e:
					print(e )
					continue
				img = fits_file[0].data
				# fig, ax = plt.subplots()
				# ax.imshow(img , vmin=250 , vmax=1000 , cmap='gray')

				# sex_output = np.loadtxt ( sex_output_name , skiprows=9 )

				# # np.savetxt ( sex_output_name , sex_output )

				# x = sex_output [ : , 5]
				# y = sex_output [ : , 6]

				# ax.scatter ( x , y) 
				# plt.show()

			# 	if True: break
		# if True: break
