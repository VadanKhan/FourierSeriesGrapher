# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:17:14 2022

@author: Vadan Khan
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#just creating the x values, input resolution & x range here
x = np.linspace(-10,10,100)
print(x)

#creating the natural number range in n, input number of terms into N
N = 100
n = np.arange(1,N+1) 
print(n)

#creating the empty arrays that will have values added to recorded in later on
yvals = np.array([])
sumvals = np.array([])

#importing the integrate function
from scipy.integrate import quad

#Inputting Desired Graph, over a period
#[here for square wave centred about y axis, with height of 1, and T=2L ]
f1 = lambda x: 1
f2 = lambda x: 0
#[assign L for period value]
L=1
bnd_1 = -L
bnd_2 = -L/2
bnd_3 = L/2
bnd_4 = L

T = 2*L
w = 2*np.pi/T

#the 1st term calculation
a_teg1, ateg1_err = quad(f2, bnd_1, bnd_2)
print(a_teg1)
a_teg2, ateg2_err= quad(f1, bnd_2, bnd_3)
print(a_teg2)
a_teg3, ateg3_err = quad(f2, bnd_3, bnd_4)
print(a_teg3)
a = (w/np.pi)*(a_teg1 + a_teg2 + a_teg3)
print(a)
#REMEMBER for fourier series formula this should be a/2


#for each value of x
for k in x: 
    #we calculate the sum of all the n range for this second term
    for h in n: 
        #attempt to integrate
        #where arbitrary integral errors assigned to same variable
        f1cos = lambda k: 1 * np.cos(h*w*k)
        f1sin = lambda k: 1 * np.sin(h*w*k)
        f2cos = lambda k: 0 * np.cos(h*w*k)
        f2sin = lambda k: 0 * np.sin(h*w*k)
        anteg1 , teg_err = quad(f2cos, bnd_1, bnd_2)
        bnteg1 , teg_err = quad(f2sin, bnd_1, bnd_2)
        anteg2 , teg_err = quad(f1cos, bnd_2, bnd_3)
        bnteg2 , teg_err = quad(f1sin, bnd_2, bnd_3)
        anteg3 , teg_err = quad(f2cos, bnd_3, bnd_4)
        bnteg3 , teg_err = quad(f2sin, bnd_3, bnd_4)
        an = (w/np.pi)*(anteg1 + anteg2 + anteg3)
        #print(an), if you want to check for processing 
        bn = (w/np.pi)*(bnteg1 + bnteg2 + bnteg3)
        #print("bn =", bn), if you want to check for processing
        sumval = an*np.cos(h*w*k) + bn*np.sin(h*w*k)
        #put it into an array
        sumvals = np.append(sumval, sumvals)
    #print(sumvals), if you want to check for processing
    #sum the the final result of the second term
    sumt = sum(sumvals)
    #!print(sumt)!
    #finally add in the average term
    y = sumt + a/2
    #collate all the y values
    yvals = np.append(yvals, y)
    sumvals = []
print(yvals)

plt.plot(x,yvals,label='fourier series')
plt.legend()
plt.show()


