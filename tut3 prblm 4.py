import numpy as np
import math
import matplotlib
from matplotlib import pyplot as ply 


def gauss(t,a=0.5,b=1,c=0):
    dat=np.exp(a/(b+(t-c)**2))
    dat+=np.random.randn(t.size)
    return dat

def Lorentz(t,a=1,b=0.5,c=0):
    dat=np.exp(-0.5*(t-c)**2/a**2)*b
    dat+=np.random.randn(t.size)
    return dat

class Lorentz:
    def __init__(self,t,a=1,b=0.5,c=0,offset=0):
        self.t=t
        self.error = np.ones(t.size)
        self.a=a
        self.b=b
        self.c=c
        offset=0
        
    def chisq(self, vec):
        a = vec[0]
        b = vec[1]
        c = vec[2]
        offset = vec[3]

        pred=offset+a/(b+(self.t-c)**2)
        chisq=np.sum((self.y-pred)**2/self.error**2)
        return chisq

def Offset(sigs):
    return sigs*np.random.randn(sigs.size)

def run_mcmc(data, start_pos, nstep, scale=None):
    nparam=start_pos.size
    params=np.zeros([nstep,nparam+1])
    params[0, 0:-1]=start_pos
    cur_chisq=data.chisq(start_pos)
    cur_pos=start_pos.copy()

    if scale==None:
        scale=np.ones(nparam)

    for i in range(1, nstep):
        new_pos=cur_pos+offset(scale)
        new_chisq=data.chisq(new_pos)
        
        if new_chisq <cur_chisq:
            accept=True

        else:
            delt=new_chisq-cur_chisq
            prob=np.exp(-0.5 * delt)

            if np.random.rand() < prob:
                accept=True

            else:
                accept=False

        if accept:
            cur_pos = new_pos
            cur_chisq = new_chisq
            
        params[i, 0:-1] = cur_pos
        params[i, -1] = cur_chisq
    return params

t = np.arange(-5, 5, 0.01)
data = Lorentz(t, a=5)

guess=np.array([1.2, 0.3, 0.3, -0.2])
scale=np.array([0.1, 0.1, 0.1, 0.1])
nstep=100000
chain=run_mcmc(data, guess, nstep, scale)
nn=int(np.round(0.2 * nstep))
chain=chain[nn:, :]  
true_param=np.array([data.a, data.b, data.c])

for i in range(0, true_param.size):

    val=np.mean(chain[:, i])
    scat=np.std(chain[:, i])
    print(true_param[i], val, scat)