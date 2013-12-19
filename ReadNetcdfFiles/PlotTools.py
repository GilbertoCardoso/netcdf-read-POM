'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

from Scientific.IO.NetCDF import NetCDFFile as Dataset
import numpy as np
import matplotlib.pyplot as plt

class PlotTools:    
    NCFileGrid = 'urias2.grid.nc'  
    def PlotVar(self, Vars):
        maskedVars = self.__MaskData__(Vars)
        plt.figure(facecolor = 'white')
        self.__MakeFourPlotVar__(maskedVars)
      
        
    def __ReadGridData__(self, GridVar): 
        NCdata = Dataset(self.NCFileGrid,'r') 
        result = NCdata.variables[GridVar][:]
        NCdata.close() 
        return result
        
    def __MaskData__(self, Vars):
        mask = self.__ReadGridData__('fsm')
        mask [mask == 0.] = np.nan
        result = [mask * var for var in Vars]
        return result
        
    def __PlotImage__(self, Var, index):
        plt.subplot(2, 2, index)
        plt.imshow(Var)
        plt.imshow(Var, interpolation='nearest', origin='lower')
        plt.axis('off')
    
    def __MakeFourPlotVar__(self, Vars):
        plt.figure(1)
        for index,var in enumerate(Vars):
            self.__PlotImage__(var,index)
        plt.show()