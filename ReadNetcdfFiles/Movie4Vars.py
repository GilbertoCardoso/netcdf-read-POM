'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

import DataTools as DataTools
import PlotTools as PlotTools 

RD = DataTools.ReadData()
PLT = PlotTools.PlotTools()

NCFile= '/home/gilk/Almacen/D/tesis/Videos/urias2.0002.nc'

AnalyzeTrasers  = ['Salinity' , 'Elevation', 'VelVerticalMeanInX','VelVerticalMeanInY']

Trasers = [ RD.ReadTrasersInNCFile(NCFile, Traser) for Traser in AnalyzeTrasers ]
TrasersIn2D = [ RD.Convert3DTrasersIn2D(traser) for traser in Trasers]

PLT.PlotVar(TrasersIn2D)

