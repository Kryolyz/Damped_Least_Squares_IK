# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:13:40 2018

@author: Kryolyz
"""

import numpy as np
from matplotlib import pyplot as plt

tp = [15,2.0]
tp[0] *= 2
tp[1] *= 2
num_links = 25
length = np.ones([num_links], dtype=np.float32)
theta = np.zeros([num_links], dtype = np.float32)
global_theta = np.zeros([num_links])
J = np.zeros([2, num_links])
damping = 12
#x(a3) = 1 * cos(a3)
#x(a2) = 1 * cos(a2) + 1 * cos(a3+a2)
#x(a1) = 1 * cos(a1) + 1 * cos(a2+a1) + 1* cos(a3+a2+a1)
#y(a3) = 1 * sin(a3)
#y(a2) = 1 * sin(a2) + 1 * sin(a3+a2)
#y(a1) = 1 * sin(a1) + 1 * sin(a2+a1) + 1 * sin(a3+a2+a1)

ee = np.zeros_like(tp)
ee[0] = 1 * np.cos(theta[0]) + 1 * np.cos(theta[1]+theta[0]) + 1 * np.cos(theta[2]+theta[1]+theta[0])
ee[1] = 1 * np.sin(theta[0]) + 1 * np.sin(theta[1]+theta[0]) + 1 * np.sin(theta[2]+theta[1]+theta[0])
error = tp - ee
err = np.linalg.norm(error)
#print(error)
its = 0
while err > 0.01:
    ee[0] = 0
    ee[1] = 0
    for i in range(num_links):
        for b in range(i+1):
            global_theta[i] += theta[b]
    for i in range(num_links):
        J[0,i] = -np.sin(global_theta[i])
        J[1,i] = np.cos(global_theta[i])
        ee[0] += np.cos(theta[i])
        ee[1] += np.sin(theta[i])
    #print(J)
    #print(ee)
    delta_theta = np.matmul(np.matmul(np.transpose(J) , np.linalg.inv(np.add(np.matmul(J,np.transpose(J)) , damping*damping*np.identity(2)))) , error)
    theta += delta_theta
    if (np.linalg.norm(delta_theta)) < 0.001:
        break
    for i in range(num_links):
        ee[0] += np.cos(theta[i])
        ee[1] += np.sin(theta[i])
    error = tp - ee
    err = np.linalg.norm(error)
    if its % 4000 == 0:
        print(error)
    its+=1
    
plt.axis([0,num_links,0,num_links])
x = []
y = []

x.append(0)
y.append(0)

px = np.zeros([num_links+1])
py = np.zeros([num_links+1])
px[0] = 0
py[0] = 0
for i in range(num_links):
    for b in range(i+1):
        px[i+1] += 1 * np.cos(theta[b])
        py[i+1] += 1 * np.sin(theta[b])
print(ee)

plt.plot(px,py)














