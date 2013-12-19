'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

from Scientific.IO.NetCDF import NetCDFFile as Dataset
import numpy as np
import matplotlib.pyplot as plt

class ReadData:
    
    def ReadNCVar(self, NCFile , NCVar):
        var = self.__ExtractData2NCFile__(NCFile, NCVar)
        return var         
    
    def __ExtractData2NCFile__(self, NCFile , Var):
        NCData = Dataset(NCFile, 'r')
        Var = NCData.variables[Var][:]
        NCData.close()
        return Var
        
    def GetFirst2DData(self, Var):
        Var = self.__RemoveTimeDimesion__(Var)      
        if self.__is3DVar__(Var): 
            Var = self.__GetVerticalAverage__(Var)
        result = Var
        return result
        
    def __is3DVar__(self, Var):
        return Var.ndim == 3
        
    def __GetVerticalAverage__(self, Var):
        zDimension = 0
        return np.average(Var,zDimension)
        
    def __RemoveTimeDimesion__(self, NCVar):
        return np.squeeze(NCVar)
        
    


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
        