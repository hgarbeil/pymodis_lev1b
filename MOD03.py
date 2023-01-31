#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 06:33:43 2023

@author: hg
"""


import numpy as np
from pyhdf.SD import SD

class MOD03 :
    
    sdfile = ''
    latlon = None ;
    geobands=[]
    minmax =[] ;
    
    def __init__(self, fname):
        self.sdfile = SD(fname)
        print (self.sdfile.info())
        datasets_dic = self.sdfile.datasets() 
        for idx, sds in enumerate(datasets_dic.keys()) :
            print(idx,sds)
        self.geobands=np.array([self.sdfile.select('Latitude'),self.sdfile.select('Longitude'),self.sdfile.select('SensorZenith')])
        print(self.geobands.shape)
        self.load_minmax()
        
    def load_minmax (self):
         min =0
         max =0
         for i in range (3):
             min=np.min(self.geobands[i])
             max=np.max(self.geobands[i])
             self.minmax.append((min,max))