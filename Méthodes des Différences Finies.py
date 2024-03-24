import numpy as np
import matplotlib.pyplot as plt 

f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x- 0.2
h = 0.01
x = np.linspace(-1 , 1)

#central differences 
dff1 = (f(x+h) - f(x-h))/(2*h)
dff2   = (f(x+h) - 2*f(x) + f(x-h))/(h**2)

#plot
plt.plot(x,f(x),'-k' , x,dff1, '--b', x,dff2, '-.r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["f(x)","f'(x)","f''(x)"])
plt.grid()
plt.show()