import random
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, cos

def buffon(L, D, N):
  hit = 0
  for loop in range(N):
    theta = pi*random.random()/2
    if (D*random.random() <= L*cos(theta)):
      hit += 1
  return hit
  
q, r = [], []
def cont_pi(N):
  L = 3
  D = 4
  Q = buffon(L, D, N)
  Pi_est = 2*N*L / (Q*D)
  q.append(Q)
  return Pi_est


L = 3
D = 4
x = np.arange(30,300,30)
y = np.zeros(len(x))
n = len(x)
for i in range(n):
  y[i] = cont_pi(x[i])

for i in range(n):
  r.append(q[i]-q[i-1])


plt.plot(x,y,'.')
plt.axhline(y=pi, color='r', linestyle='-')
plt.xlabel('N (ukuran sample)')
plt.ylabel('$\pi$')
plt.title('Buffons Needle')
plt.show()
print('NILAI RATA-RATA PI')
print(round((sum(y)/n),3),'\n')
print('NILAI PI DISETIAP PERCOBAAN')
print(y,'\n')
print('NILAI Q DISETIAP PERCOBAAN')
print(q,'\n')