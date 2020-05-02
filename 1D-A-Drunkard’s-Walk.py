import random
from matplotlib import pyplot as plt

# inisialisasi banyak langkah dalam 1x simulasi
N_steps = 200

# panjang langkah tiap kali menlangkah
range_step = 1

# inisialisasi gambah grafik
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 25.1)
ax.set_ylim(0, 25.1)

# inisialisasi langkah awal
x, y = [], []
x.append(random.randint(1,25))
y.append(random.randint(1,25))

# inisialisasi langkah berikutnya
next_step = ['xplus', 'yplus']


for i in range(N_steps-1):
  ax.scatter(x[i],y[i], c='k')
# random untuk langkah berikutnya
  new_step = random.choice(next_step)
  if new_step == 'xplus':
# kondisi untuk tidak melewati gambar grafik yang telah ditenttukan
    if x[i] >= 25 or y[i] >= 25:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i]+range_step)
      y.append(y[i])
  else:
# kondisi untuk tidak melewati gambar grafik yang telah ditenttukan
    if x[i] >= 25 or y[i] >= 25:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i])
      y.append(y[i]+range_step)
  ax.scatter(x[i],y[i], c='r')
  plt.pause(0.1)
  
plt.show()
