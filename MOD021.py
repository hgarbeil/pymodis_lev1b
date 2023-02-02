#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 05:28:12 2023

@author: hg
"""

import numpy as np
from pyhdf.SD import SD

class MOD021 :
    
    sdfile = ''
    thermalarr = None ;
    bands=[]
    minmax =[] ;
    
    def __init__(self, fname):
        print(fname)
        self.sdfile = SD(fname)
        print (self.sdfile.info())
        datasets_dic = self.sdfile.datasets() 
        # for idx, sds in enumerate(datasets_dic.keys()):
        #     print(idx, sds)
        self.read_thermal()
        self.load_minmax()
        
    def read_thermal (self):
        # select the emissive thermal bands
        band_1k = self.sdfile.select('EV_1KM_Emissive')
        # b11 is 32, b2 is 22 - see array below to get 21,22,32
        emiss_bands=[1,2,11]
        
        
        for ib0 in range(3):
            ib = emiss_bands[ib0]
            atts=band_1k.attributes()
            # get calibration values
            scales = atts['radiance_scales']
            offs = atts['radiance_offsets']
            #print(scales)
            b22 = band_1k[ib,:,:]
            #apply calibration
            band22 = (b22-offs[ib]) * scales[ib] 
            #print(np.max(band22))
        
            self.bands.append(band22)
        self.thermalarr = np.array([self.bands[0],self.bands[1],self.bands[2]])
        
    def load_minmax (self):
        min =0
        max =0
        for i in range (3):
            min=np.min(self.thermalarr[i])
            max=np.max(self.thermalarr[i])
            self.minmax.append((min,max))
            
     
        
        
        