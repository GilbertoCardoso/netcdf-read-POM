'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

from Scientific.IO.NetCDF import NetCDFFile as Dataset
import numpy as np

class ReadData:
    
    def ReadNCVar(self, NCFile , NCVar):
        var = self.__ExtractData2NCFile__(NCFile, NCVar)
        return var         
    
    def __ResolvAliasVars__(self, IdiomaticName):
        VarsAliasList = {'Salinity' : 's', 'Elevation' :'elb' , 'VelVerticalMeanInX' : 'uab' ,'VelVerticalMeanInY': 'vab'}
        return VarsAliasList(IdiomaticName)
    
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
        