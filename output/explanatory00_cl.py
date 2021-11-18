import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/z5278074/Desktop/class_transportrate_15102021/output/explanatory00_cl.dat', '/Users/z5278074/Desktop/class_transportrate_15102021/output/transportrate00_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['explanatory00_cl', 'transportrate00_cl']

fig, ax = plt.subplots()
y_axis = []
tex_names = []
x_axis = 'l'
ax.set_xlabel('$\ell$', fontsize=16)
plt.show()