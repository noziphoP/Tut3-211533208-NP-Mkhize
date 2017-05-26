import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.linspace(0,2*np.pi,N)
y = np.sin(x)
z=np.cos(x)
mydata = y+np.random.randn(x.size)
order = 10

def fit(x,N,order):
    a=np.zeros([x.size,order])
    a[:,0] = 1.0
    
    for i in range(1,order):
        a[:,i]=A[:,i-1]*x
    a=np.matrix(A)
    d=np.matrix(data).transpose()
    lhs=a.transpose()*a
    rhs=a.transpose()*d
    fitp=np.linalg.inv(lhs)*rhs
    pred=a*fitp

plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,mydata,'*')
plt.plot(x,pred,'r')

plt.show()

