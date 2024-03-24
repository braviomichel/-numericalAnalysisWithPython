from IPython.display import display, Latex
from IPython.core.display import HTML
%reset -f
%matplotlib inline
%autosave 300
from matplotlib.pylab import *

from scipy.sparse import  spdiags

#importation des bibliothèques utiles
from scipy.sparse.linalg import spsolve
from scipy.sparse import spdiags
# le pas h
N=600
h=1/(N+1)
# construction du vecteur de discrétisation
x=linspace(h,1-h,N)
x_avec_CL=linspace(0,1,N+2)
#construction de la fonction f de votre choix
f=lambda x : 150*x**2-100*x
#construction du second membre du systeme
F=f(x)
#construction de la matrice en systeme creux
D0=2/h**2*ones(N)
D1=-1/h**2*ones(N)
A=spdiags(D0,[0],N,N)+spdiags(D1,[1],N,N)+spdiags(D1,[-1],N,N)
#resolution du systeme creux
U=spsolve(A,F)
#Ajout des CL de Dirichlet
U_avec_CL=zeros(N+2)
U_avec_CL[1:N+1]=U
plot(x_avec_CL,U_avec_CL)
#On rajoute les points de discrétisation sur l'axe des abscisses.
scatter(x,0*x,[0.1],'red')
