import random
from matplotlib import pyplot as plt

# inisialisasi berapa banyak langkah dalam 1x simulasi
N_steps = 200

# inisisalisasi panjang langkah tiap kali melangkah
range_step = 1

# inisialisasi besar gambar grafik
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 25.1)
ax.set_ylim(0, 25.1)

# inisialisasi langkah awal
x, y = [], []
x.append(random.randint(1,25))
y.append(random.randint(1,25))

# inisialisasi langkah berikutnya
next_step = ['xplus', 'yplus', 'xmin', 'ymin']

for i in range(N_steps-1):
  ax.scatter(x[i],y[i], c='k')
# random langkah berikutnya
  new_step = random.choice(next_step)
  if new_step == 'xplus':
# kondisi untuk tidak melewati batas gambar grafik yang telah ditentukan
    if x[i] >= 25 or y[i] >= 25 or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i]+range_step)
      y.append(y[i])
  elif new_step == 'yplus':
# kondisi untuk tidak melewati batas gambar grafik yang telah ditentukan
    if x[i] >= 25 or y[i] >= 25 or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i])
      y.append(y[i]+range_step)
  elif new_step == 'xmin':
# kondisi untuk tidak melewati batas gambar grafik yang telah ditentukan
    if x[i] >= 25 or y[i] >= 25or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i]-range_step)
      y.append(y[i])
  else:
# kondisi untuk tidak melewati batas gambar grafik yang telah ditentukan
    if x[i] >= 25 or y[i] >= 25 or x[i]<=1 or y[i]<=1:
      x.append(random.randint(1,15))
      y.append(random.randint(1,15))
    else:
      x.append(x[i])
      y.append(y[i]-range_step)
  ax.scatter(x[i],y[i], c='r')
# fungsi output untuk pause
  plt.pause(0.1)

plt.show()
