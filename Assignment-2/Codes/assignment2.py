# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1McGJza9WyhS6yYaywDpbuDVa0B7Ze8bw
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt


def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

a=-3
b=2
A = np.array([a,0]) 
B = np.array([0,b]) 
x1=-3
x2=0
y1=0
y2=2

m=(y2-y1)/(x2-x1)
print(m)

x_AB=line_gen(A,B)


plt.plot(x_AB[0,:],x_AB[1,:],label='$2x-3y+6=0$')


plt.grid() # minor
plt.plot(A[0], A[1],'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left')

plt.show()

