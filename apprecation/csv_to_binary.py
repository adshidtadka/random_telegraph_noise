#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 22:30:19 2018

@author: mahfuz
"""
import numpy as np
from glob import glob
import re
import scipy.io as sio 


import matplotlib
import matplotlib.pyplot as plt

font = {'size' : 21}
matplotlib.rc('font', **font)
matplotlib.rcParams['lines.linewidth'] = 2

data_dir = '180518_bak/'

data_dict = {}
for file in glob(data_dir + '*.csv'):
    m = re.search('[\w/]+(ch\d+v\d+r\d+(s\d+)\w+)', file)
    name = m.group(1)
    s = m.group(2)
    data = np.loadtxt(file, delimiter=',')
    data_dict[s] = data

print('Number of section: ', len(data_dict))

# save as binary data in matlab format
name = name.replace(s, '')
print(name)
sio.savemat('180518_' + name + '.mat', data_dict)

# plot data
s = 's269'
data = data_dict[s]

plt.cla()
plt.plot(np.array(range(data.size)) / 1000, 100*(data-data.min())/data.min(), 'ko-', markersize=4, label='pMOSFET')
plt.xlabel('Time [s]')
plt.ylabel('$\Delta f / f$ [%]')
#plt.legend()
plt.grid()
plt.show()
