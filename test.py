#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:33:59 2023

@author: hg


"""
import pathlib
import numpy as np
import os, sys

from MOD021 import *
from MOD03 import *


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

m = MOD021 (sys.argv[1])
ll = MOD03 (sys.argv[2])
print (m.minmax)
print (ll.minmax)