import math
from matplotlib.pylab import *
%matplotlib inline

from scipy.optimize import fsolve

#initialisation

t0 = 0.
tfinal = 1.
y0 = 1.


#solution exacte

def sol_exacte(t):
    return y0*math.exp(t**2)


#equation différentiellle

def phi(t,y):
    return 2.*y*t


#discrétisation

N = 8
h = (tfinal-t0)/N
tt = [ t0+i*h for i in range(N+1) ]


#euler explicite

def euler_progressif(phi,tt):
    uu = [y0]
    for i in range(N):
        uu.append(uu[i]+h*phi(tt[i],uu[i]))
    return uu


#euler implicite

def euler_regressif(phi,tt):
    uu = [y0]
    for i in range(N):
        temp = fsolve(lambda x: -x+uu[i]+h*phi(tt[i+1],x), uu[i])
        uu.append(temp)
    return uu

#Cranck-Nicolson

def CN(phi,tt):
    uu = [y0]
    for i in range(len(tt)-1):
        temp = fsolve(lambda x: -x+uu[i]+0.5*h*( phi(tt[i+1],x)+phi(tt[i],uu[i]) ), uu[i])
        uu.append(temp)
    return uu

#calculs

yy = [sol_exacte(t) for t in tt]

uu_ep   = euler_progressif(phi,tt)

uu_er   = euler_regressif(phi,tt)
uu_CN   = CN(phi,tt)




#affichage

figure()
plot(tt,yy,'b-',tt,uu_ep,'r-D')
title('Euler explicite - max(|erreur|)=%1.10f'%(max([abs(uu_ep[i]-yy[i]) for i in range(N+1)])))


figure()
plot(tt,yy,'b-',tt,uu_er,'r-D')
title('Euler implicite - max(|erreur|)=%1.10f'%(max([abs(uu_er[i]-yy[i]) for i in range(N+1)])))

figure()
plot(tt,yy,'b-',tt,uu_CN,'r-D')
title('Crank Nicolson - max(|erreur|)=%1.10f'%(max([abs(uu_CN[i]-yy[i]) for i in range(N+1)])))

show()








