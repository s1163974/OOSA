import h5py
import numpy as np



####################################################################################################

#def readarr():
'''fuction to read an array'''
filename="/geos/netdata/oosa/week4/lvis_antarctica/ILVIS1B_AQ2015_1014_R1605_070717.h5"
f=h5py.File(filename,'r')

#see whats is inside
list(f)

# read a value into RAM
lon0=np.array(f['LON0'])
#or a slice
lon0=np.array(f['LON0'])[0:100]

#print array
print(lon0)


