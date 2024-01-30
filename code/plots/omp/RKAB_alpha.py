import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_alpha.py

filename = "outputs/omp/RKAB_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
for i in range(file_size):
	it.append(int(lines[i].split()[3]))

it = it[0::2]

it_2_80000_1000_50 = it[0:6]
it_2_80000_1000_500 = it[6:12]
it_2_80000_1000_1000 = it[12:18]

it_4_80000_1000_50 = it[18:24]
it_4_80000_1000_500 = it[24:28]
it_4_80000_1000_1000 = it[28:32]

it_2_80000_4000_500 = it[32:38]
it_2_80000_4000_1000 = it[38:44]
it_2_80000_4000_4000 = it[44:50]

it_4_80000_4000_500 = it[50:55]
it_4_80000_4000_1000 = it[55:60]
it_4_80000_4000_4000 = it[60:63]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

alpha_2 = [1.0, 1.2, 1.3, 1.5, 1.8, 1.99864]
alpha_4 = [1.0, 1.5, 2.0, 2.5, 3.0, 3.99183]

fig = plt.figure(figsize=(10, 7))
plt.axvline(x=1.99864, ymin=0, ymax=2**10, linewidth=1.5, linestyle='--', color='black', label=r'$\alpha^*$')
# plt.scatter(alpha_2[:len(it_2_80000_1000_50)], it_2_80000_1000_50, color='orange')
plt.plot(alpha_2[:len(it_2_80000_1000_50)], it_2_80000_1000_50, linewidth=1.5, color='orange', label=r'Block Size = 50', marker='s', markersize=10)
# plt.scatter(alpha_2[:len(it_2_80000_1000_500)], it_2_80000_1000_500, color='red')
plt.plot(alpha_2[:len(it_2_80000_1000_500)], it_2_80000_1000_500, linewidth=1.5, color='red', label=r'Block Size = 500', marker='o', markersize=10)
# plt.scatter(alpha_2[:len(it_2_80000_1000_1000)], it_2_80000_1000_1000, color='blue')
plt.plot(alpha_2[:len(it_2_80000_1000_1000)], it_2_80000_1000_1000, linewidth=1.5, color='blue', label=r'Block Size = 1000', marker='X', markersize=10)
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_alpha_it_80000_1000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.axvline(x=3.99183, ymin=0, ymax=2**10, linewidth=1.5, linestyle='--', color='black', label=r'$\alpha^*$')
# plt.scatter(alpha_4[:len(it_4_80000_1000_50)], it_4_80000_1000_50, color='orange')
plt.plot(alpha_4[:len(it_4_80000_1000_50)], it_4_80000_1000_50, linewidth=1.5, color='orange', label=r'Block Size = 50', marker='s', markersize=10)
# plt.scatter(alpha_4[:len(it_4_80000_1000_500)], it_4_80000_1000_500, color='red')
plt.plot(alpha_4[:len(it_4_80000_1000_500)], it_4_80000_1000_500, linewidth=1.5, color='red', label=r'Block Size = 500', marker='o', markersize=10)
# plt.scatter(alpha_4[:len(it_4_80000_1000_1000)], it_4_80000_1000_1000, color='blue')
plt.plot(alpha_4[:len(it_4_80000_1000_1000)], it_4_80000_1000_1000, linewidth=1.5, color='blue', label=r'Block Size = 1000', marker='X', markersize=10)
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_alpha_it_80000_1000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

alpha_2 = [1.0, 1.2, 1.3, 1.5, 1.8, 1.99976]
alpha_4 = [1.0, 1.5, 2.0, 2.5, 3.0, 3.99857]

fig = plt.figure(figsize=(10, 7))
plt.axvline(x=1.99976, ymin=0, ymax=2**10, linewidth=1.5, linestyle='--', color='black', label=r'$\alpha^*$')
# plt.scatter(alpha_2[:len(it_2_80000_4000_500)], it_2_80000_4000_500, color='orange')
plt.plot(alpha_2[:len(it_2_80000_4000_500)], it_2_80000_4000_500, linewidth=1.5, color='orange', label=r'Block Size = 500', marker='o', markersize=10)
# plt.scatter(alpha_2[:len(it_2_80000_4000_1000)], it_2_80000_4000_1000, color='red')
plt.plot(alpha_2[:len(it_2_80000_4000_1000)], it_2_80000_4000_1000, linewidth=1.5, color='red', label=r'Block Size = 1000', marker='X', markersize=10)
# plt.scatter(alpha_2[:len(it_2_80000_4000_4000)], it_2_80000_4000_4000, color='blue')
plt.plot(alpha_2[:len(it_2_80000_4000_4000)], it_2_80000_4000_4000, linewidth=1.5, color='blue', label=r'Block Size = 4000', marker='*', markersize=10)
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_alpha_it_80000_4000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.axvline(x=3.99857, ymin=0, ymax=2**10, linewidth=1.5, linestyle='--', color='black', label=r'$\alpha^*$')
# plt.scatter(alpha_4[:len(it_4_80000_4000_500)], it_4_80000_4000_500, color='orange')
plt.plot(alpha_4[:len(it_4_80000_4000_500)], it_4_80000_4000_500, linewidth=1.5, color='orange', label=r'Block Size = 500', marker='o', markersize=10)
# plt.scatter(alpha_4[:len(it_4_80000_4000_1000)], it_4_80000_4000_1000, color='red')
plt.plot(alpha_4[:len(it_4_80000_4000_1000)], it_4_80000_4000_1000, linewidth=1.5, color='red', label=r'Block Size = 1000', marker='X', markersize=10)
# plt.scatter(alpha_4[:len(it_4_80000_4000_4000)], it_4_80000_4000_4000, color='blue')
plt.plot(alpha_4[:len(it_4_80000_4000_4000)], it_4_80000_4000_4000, linewidth=1.5, color='blue', label=r'Block Size = 4000', marker='*', markersize=10)
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_alpha_it_80000_4000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()