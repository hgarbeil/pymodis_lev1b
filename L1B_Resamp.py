#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 07:11:44 2023

@author: hg
"""
from MOD021 import *
from MOD03 import *


import numpy as np 

class L1B_Resamp :
    ThermFile=None 
    GeoFile=None
    llbounds=[20.5, -156.3, 18.75, -154.6]
    llspace = .0068
    outarr = None
    
    def __init__(self):
        self.ns = int((self.llbounds[3] - self.llbounds[1])/self.llspace+1)
        self.nl = int((self.llbounds[0] - self.llbounds[2])/self.llspace+1)
        print (self.nl, self.ns)
        self.outarr = np.zeros((self.nl,self.ns),dtype=np.float32)
        
        
    def set_arrays (self, m21, m3):
        self.thermbands = m21.thermalarr
        self.geobands = m3.geobands
        print (self.thermbands.shape)
        
    def resamps (self) :
        shape_raw = self.thermbands.shape
        print (shape_raw[1])
        for i in range(shape_raw[1]):
            for j in range (shape_raw[2]):
                yloc = int((self.llbounds[0] - self.geobands[0,i,j]) / self.llspace+0.5)
                xloc = int((self.geobands[1,i,j] - self.llbounds[1]) / self.llspace+0.5)
                #print(xloc,yloc)
                if yloc < 0 or yloc >= self.nl :
                    continue 
                if xloc < 0 or xloc >= self.ns :
                    continue 
                self.outarr[yloc,xloc]= self.thermbands[1,yloc,xloc]
                
        