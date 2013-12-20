'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

import DataTools as DataTools
import PlotTools as PlotTools 

RD = DataTools.ReadData()
PLT = PlotTools.PlotTools()

NCFile= 'urias2.0002.nc'
AnalyzedVars  = ['Salinity' , 'Elevation', 'VelVerticalMeanInX','VelVerticalMeanInY']


Vars = [ RD.ReadVarsInNCFile(NCFile,v) for v in AnalyzedVars ]

AnalyzedVarsIn2D = [ RD.Convert3DVarsIn2D(v) for v in Vars]

PLT.PlotVar(AnalyzedVarsIn2D)

