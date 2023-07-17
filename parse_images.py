import numpy as np
import astropy as ap
from astropy.io import fits

import os
from os.path import isdir, isfile, join

dir_name = './data/'

file_names = [dir_name + f for f in os.listdir(dir_name) if isfile(join(dir_name,f)) ]
print(len(file_names))



directory = './refactor'


input_file = np.loadtxt('input.csv', dtype=object, skiprows=1, usecols=(i for i in range(25)), delimiter=',')

'''
ex fits info

Filename: 1851148p.fits.fz
No.    Name      Ver    Type      Cards   Dimensions   Format
  0  PRIMARY       1 PrimaryHDU     466   ()      
  1  ccd00         0 CompImageHDU    502   (2112, 4644)   int16   
  2  ccd01         1 CompImageHDU    502   (2112, 4644)   int16   
  3  ccd02         2 CompImageHDU    502   (2112, 4644)   int16   

...and so on...

'''



cts = 0

for f in file_names:
	try:
		file = fits.open ( f )

		# print(f)
	except Exception as e:
		print('broke at ', f , e)
		continue
	print(f)

	# print ( len ( file ) )

	f_id = f.split('/')[-1].split('p')[0]
	
	primary_hdu = file[0]
	target_id = primary_hdu.header['OBJECT']
	
	# print ( f_id )
	# print(target_id)

	out_dir = '/'.join( [directory , target_id ] )
	if not isdir (out_dir) : os.mkdir ( out_dir )

	out_dir = '/'.join( [directory , target_id , f_id ] )
	if not isdir (out_dir) : os.mkdir ( out_dir )	
	
	# print(out_dir)
	# print()

	try:
		
		for i in range(1,len(file)) : 

			fits_image  = file[i].data 
			fits_header = file[i].header

			c     = fits_header['EXTVER']			

			save_to = out_dir + '/' + f_id + 'on' + str(c) + '.fits'
			print(save_to)
			fits.writeto ( save_to , fits_image , header=fits_header , overwrite=True  )
	except Exception as e:
		print(e)
		continue
	file.close ()
	print()

	# if True: break

	
