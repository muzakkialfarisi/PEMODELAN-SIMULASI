import matplotlib.pyplot as plt
import random

N_steps = 200

range_step = 1

fig, ax = plt.subplots()
ax.set_xlim(0, 25.1)
ax.set_ylim(0, 25.1)

x, y = [], []
x.append(random.randint(1,25))
y.append(random.randint(1,25))


next_step = ['xplus', 'yplus', 'xmin', 'ymin']
for i in range(N_steps-1):
  ax.scatter(x[i],y[i], c='k') 
  new_step = random.choice(next_step)
  plt.pause(0.1)
  if new_step == 'xplus':
    if x[i] >= 25 or y[i] >= 25 or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i]+range_step)
      y.append(y[i])
  elif new_step == 'yplus':
    if x[i] >= 25 or y[i] >= 25 or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i])
      y.append(y[i]+range_step)
  elif new_step == 'xmin':
    if x[i] >= 25 or y[i] >= 25or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i]-range_step)
      y.append(y[i])
  else:
    if x[i] >= 25 or y[i] >= 25 or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i])
      y.append(y[i]-range_step)
  ax.scatter(x[i],y[i], c='r')
  ax.plot(x,y)

ax.scatter(x[0],y[0], c='k',)
ax.scatter(x[len(x)-1],y[len(y)-1], c='k')
plt.show()