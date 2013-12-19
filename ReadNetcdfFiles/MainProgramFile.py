'''
Created on Dec 18, 2013
Program to read Necdf Data Files
@author: Gilberto Cardoso
'''

import DataTools as DataTools

RD = DataTools.ReadData()
plt = DataTools.PlotTools()

NCFile= 'urias2.0002.nc'
NCVars = ['s', 'elb', 'uab', 'vab']


Vars = [ RD.ReadNCVar(NCFile,v) for v in NCVars ]

first2DData = [ RD.GetFirst2DData(v) for v in Vars]

plt.PlotVar(first2DData)
