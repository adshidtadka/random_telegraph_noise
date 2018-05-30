#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 22:30:19 2018

@author: mahfuz
"""
import numpy as np
import scipy.io as sio 
#from scipy import stats

import matplotlib
import matplotlib.pyplot as plt

font = {'size' : 21}
matplotlib.rc('font', **font)
matplotlib.rcParams['lines.linewidth'] = 2

# read binary data
data = sio.loadmat('../matfiles/180518_ch02v050r0d3_int252_time10000.mat')

plt.cla()
nrows = 4
ncols = 4
sstart = 0
for ii in range(nrows*ncols):
    plt.subplot(nrows, ncols, ii+1)
    plt.cla()
    s = 's'+str(sstart+ii)
    y = data[s].flatten()
    x = np.array(range(y.size))
    plt.plot(x, y, 'k-', label=s)
    plt.xticks([])
    plt.legend()
    

#plt.xlabel('$f_\mathrm{max}$ [a.u.]')
#plt.ylabel('$\Delta f / f$ [%]')


#plt.legend()
#plt.grid()
plt.show()
