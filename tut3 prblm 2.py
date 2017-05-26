import numpy as np

class particles:
    def __init__(self, N=1000, soften=0.1,m=1,dt=0.01):
        self.options = {}  
        self.options['dt'] = dt
        self.options['G'] = 1.0             
        self.options['soften'] = soften
        self.options['N'] = N                    
        self.x=np.random.randn(N)
        self.y=np.random.randn(N)
        self.m=np.ones(N)
        self.vx=np.zeros(N)
        self.vy=np.zeros(N)
        self.options={} 
    
class Particles:
    def __init__(self,x1=0,x2=1,y1=0,y2=1,m1=5,m2=10,n=2,G=9.8):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.m1=m1
        self.m2=m2
        self.opts={}
        self.opts[n]=2
        self.opts[G]=9.8
    def Potential(self):
        pot=numpy((G*self.m1,self.m2)/((self.x2-self.x1)-(self.y2-self.y1)))
        potential = np.zeros(self.options['N'])
    for i in range(0, self.options['N']):
        for j in range(0, self.options['N']):
        
                    if (i != j):
                        xarr = self.x[i] - self.x[j]
                        yarr = self.y[i] - self.y[j]
                        radius = np.sqrt(xarr ** 2 + yarr ** 2)
                        potential[i] = potential[i] + self.m[i] * self.m[j] * self.options['G'] * 1.0 / radius
                    return potential        
        if __name__=='__main__':
            part=Particles()
            pot=part.Potential()  
        return potential

#2b

    def force(self):    
        self.fx = np.zeros(self.options['N'])
        self.fy = np.zeros(self.options['N'])
        potential = np.zeros(self.options['N'])

        for i in range(0, self.options['N'] - 1):
            for j in range(i + 1, self.options['N']):
                xarr = self.x[i] - self.x[j]
                yarr = self.y[i] - self.y[j]
                radius2 = xarr ** 2 + yarr ** 2
                softened = self.options['soften'] ** 2



                if radius2 < softened:
                    radius2 = softened
                    
                    
                radius = np.sqrt(radius2)
                Rnew = radius * radius2            


                self.fx[i] = self.fx[i] - xarr * (1.0 / Rnew) * self.m[j]
                self.fy[i] = self.fy[i] - yarr * (1.0 / Rnew) * self.m[j]
                self.fx[j] = self.fx[j] + xarr * (1.0 / Rnew) * self.m[i]
                self.fy[j] = self.fy[j] + yarr * (1.0 / Rnew) * self.m[i]



                potential[i] = potential[i] + self.m[i] * self.m[j] * self.options['G'] * 1.0 / radius
                
            return potential.sum()   
        

#2c
    def Update(self, dt=0.01):         

        self.x = self.x + self.vx * self.options['dt']
        self.y = self.y + self.vy * self.options['dt']

        potential = self.force()

        self.vx = self.vx + self.fx * self.options['dt']
        self.vy = self.vy + self.fy * self.options['dt']

        return potential.sum()

nclass = NbodySolver()

print ('energy is ', nclass.force())


potentialvar = np.zeros(100)
kineticvar = np.zeros(100)
dx = 0

while (dx < 100):

    finalPotential = nclass.Update(0.05)
    kineticenergy = np.sum(nclass.m * (nclass.vx ** 2 + nclass.vy ** 2))

    print ('Total energy is ', [finalPotential, kineticenergy, kineticenergy - 2.0 * finalPotential])

    plt.plot(nclass.x, nclass.y, 'b*') 
    
#2d

plt.show()
potentialvar[dx] = finalPotential
kineticvar[dx] = kineticenergy