# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 19:02:50 2014

@author: fran
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

N=1000000 ; 'numero de puntos'
n=1000 ; 'numero de bines'

m=2147483647 ;'modulo'
a=16807 ; 'multiplicador'
c=0 ; 'constante'
x0=10 ; 'semilla'

X=[]
for i in range(N):
    x=(a*x0+c)%m
    "Almacenamos la diferencia al cuadrado de dos puntos unidimensionales"
    X+=[((x-x0)**2/float(m*m))]
    x0=x
    
"""x=np.linspace(min(X),max(X),num=1000)
param=ss.expon.fit(X)
pdf_fitted=ss.expon.pdf(x,loc=param[0],scale=param[1])"""


plt.hist(X,n)
"plt.plot(x,pdf_fitted)"
plt.yscale('log')



plt.show()