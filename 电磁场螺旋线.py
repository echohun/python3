from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

figure=plt.figure()
ax=figure.add_subplot(111,projection='3d')

t=np.linspace(0,10,10000)
Ex = 2*np.cos(2*np.pi*(3*(10**8)*t))
Ey = 2*np.cos(2*np.pi*(3*(10**8)*t-1/4))
ax.plot(Ex,Ey,t)

#z=np.linspace(0,10,1000)
#Ex = 2*np.cos(2*np.pi*z)
#Ey = 2*np.cos(2*np.pi*(-z-1/4))
#ax.plot(Ex,Ey,z)
plt.show()
