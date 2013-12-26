'''
Created on Dec 26, 2013 
@author: gilk
'''
def DeterminePathFiles(Path, NameExperiment,  PathNumber):
    PathNumberStringWithCeros = str(PathNumber).zfill(4)
    return Path + NameExperiment + '.' + PathNumberStringWithCeros + '.nc'
