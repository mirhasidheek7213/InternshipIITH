# -*- coding: utf-8 -*-
"""Assignment4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QBMRyaOMl5AjiXbWsBqX6Wvm3kwrf6UK
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

xx, yy = np.meshgrid(range(10), range(10))
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


A = np.array([3,6,9]).reshape((3,1))
B = np.array([10,20,30]).reshape((3,1))
C = np.array([25,-41,5]).reshape((3,1))

def line_gen(A,B):
  len =10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)



plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CA[0,:],x_CA[1,:],x_CA[2,:],label="CA")


ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.text(3,6,9, "A", color='red')
ax.text(10,20,30, "B", color='red')
ax.text(25,-41,5, "C", color='red')


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()