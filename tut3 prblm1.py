import numpy as np
class Particles:
   def __init__(self,x1=0,x2=1,y1=0,y2=1,m1=5,m2=10,n=2,G=1):
      self.x1=x1
      self.x2=x2
      self.y1=y1
      self.y2=y2
      self.m1=m1
      self.m2=m2
      self.opts={}
      self.opts[n]=2
      self.opts[G]=1
      
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
   
   
   
   