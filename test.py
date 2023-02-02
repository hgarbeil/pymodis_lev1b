#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:33:59 2023

@author: hg


"""
import pathlib
import numpy as np
import os, sys
import matplotlib.pyplot as plt

from MOD021 import *
from MOD03 import *
from L1B_Resamp import *



# infile = sys.argv[1]

# file = SD(infile)
# (a,b) = file.info()
# datasets_dic = file.datasets()

# for idx, sds in enumerate(datasets_dic.keys()):
#     print(idx, sds)
    

# band_1k = file.select('EV_1KM_Emissive')
# # b11 is 32, b2 is 22

# atts=band_1k.attributes()
# scales = atts['radiance_scales']
# offs = atts['radiance_offsets']
# print(scales)
# b22 = band_1k[2,:,:]
# print(b22.shape)
# band22 = (b22+offs[2]) * scales[2] 
# print(np.max(band22))
fpairs=[]

indir = '/Users/hg/workdir/data/'
# get pairs of MOD21 MOD03 files
lfiles=os.listdir(indir)
for f in lfiles :
    if 'MOD021KM' in f :
        indx = f.find('A2022')
        srch_string = f[indx:indx+12]
        for f03 in lfiles :
            if 'MOD03' in f03 and srch_string in f03 :
                fpairs.append((indir+f,indir+f03))
for p in fpairs:
    print(p)
    #print (p[0])
                
    m = MOD021 (p[0].strip())
    ll = MOD03 (p[1].strip())
    l1br = L1B_Resamp()
    l1br.set_arrays(m,ll)
    l1br.resamps()
    
    plt.imshow(m.thermalarr[2,:,:],cmap='gray')
    #plt.imshow(l1br.outarr,cmap='gray')
    plt.show()
