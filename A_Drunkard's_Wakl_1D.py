import random
import matplotlib.pyplot as plt

N_steps = 200

range_step = 1

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 25.1)
ax.set_ylim(0, 25.1)

x, y = [], []
x.append(random.randint(1,25))
y.append(random.randint(1,25))

next_step = ['xplus', 'yplus']
for i in range(N_steps-1):
  ax.scatter(x[i],y[i], c='k')
  plt.pause(0.1)
  new_step = random.choice(next_step)
  if new_step == 'xplus':
    if x[i] >= 25 or y[i] >= 25:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i]+range_step)
      y.append(y[i])
  else:
    if x[i] >= 25 or y[i] >= 25:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i])
      y.append(y[i]+range_step)
  ax.scatter(x[i],y[i], c='r')

ax.scatter(x[len(x)-1],y[len(y)-1], c='b')
ax.scatter(x[0],y[0], c='g', marker='x')
plt.show()