'''note to self:lvisClass is a py file stored in week 4 folder, 
this imports the class :lvisData and the methods the read it.
then reproject the data  '''

from lvisClass import lvisData
from pyproj import Proj, transform # package for reprojecting data
import matplotlib as plt


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
  def plotWaveforms(self,wF_dict):
        if not hasattr(self, 'waves') or not hasattr(self, 'z'):
            raise AttributeError("lvisData class must have 'waves' and 'z' attributes.")
    
           # Create plots and save as PNG files
        for i in range(self.nWaves):
            fig, ax = plt.subplots()
            ax.plot(self.z[i], self.waves[i])
            ax.set_xlabel('Elevation (meters)')
            ax.set_ylabel('Waveform Intensity')
            ax.set_title(f'Waveform Plot - Shot {self.lShot[i]}')
            
            # Save the plot as a PNG file
            output_filename = f"{wF_dict}/waveform_plot_{i + 1}.png"
            plt.savefig(output_filename)
            
            # Close the plot to free up resources
            plt.close() 



#a = reprojectarr(lvisData)
if __name__ == '__main__':
    a = reprojectarr(filename = "/geos/netdata/oosa/week4/lvis_antarctica/ILVIS1B_AQ2015_1014_R1605_070717.h5")
    a.reprojectData(3031)
    #save png file here
    wF_dict = "/home/s1163974/OOSA/week4"
    a.plotWaveforms(wF_dict)
    #print(a)

    ### png not appearing. need to look at work again.
    ###terminal slow