'''note to self:lvisClass is a py file stored in week 4 folder, 
this imports the class :lvisData and the methods the read it.
then reproject the data  '''

from lvisClass import lvisData
from pyproj import Proj, transform # package for reprojecting data



#class lvisData(object):
'''
  LVIS data handler
  '''

#Parent class:lvisData
#Child class:reprojectarr (inherits from parent class)
#This is vector!  
class reprojectarr(lvisData):
  def reprojectData(self, outEPSG):
    # reproject data to be in metres
    inProj=Proj(init="epsg:4326")
    outProj=Proj(init="epsg:"+str(outEPSG))
    # reproject data from EPSG to meters
    x,y=transform(inProj,outProj,self.lon,self.lat)
    return(x,y)


#a = reprojectarr(lvisData)
if __name__ == '__main__':
    a = reprojectarr(filename = "/geos/netdata/oosa/week4/lvis_antarctica/ILVIS1B_AQ2015_1014_R1605_070717.h5")
    a.reprojectData(3031)
    print(a)