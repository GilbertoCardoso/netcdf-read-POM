'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

AnalyzeTrasers  = ['Salinity' , 'Elevation', 'VelVerticalMeanInX','VelVerticalMeanInY']

PathFiles = '/home/gilk/Almacen/R/respaldoGil/gilk/doctorado/trajul2012/purias_2012/out/'
NameFileExperiment = 'urias2' 

import DataTools as DataTools
import PlotTools as PlotTools
import PathsFilesTools as FT 

DT = DataTools.ReadData()
PlT = PlotTools.PlotTools()

for PathNumber in range(2):
    DataFileAnalized =  FT.DeterminePathFiles( PathFiles,  NameFileExperiment, PathNumber)
    Trasers = [ DT.ReadTrasers(DataFileAnalized, Traser) for Traser in AnalyzeTrasers ]
    TrasersIn2D = [ DT.Convert3DTrasersIn2D(traser) for traser in Trasers]
    PlT.PlotVar(TrasersIn2D)
