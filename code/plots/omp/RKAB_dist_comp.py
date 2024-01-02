import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_dist_comp.py

filename = "outputs/omp/RK.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
it_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))
	it_seq.append(int(lines[i].split()[3]))

indices = (10, 16, 18, 24, 26, 27, 33, 35, 36, 43, 45, 46)
time_seq_dim = [time_seq[i] for i in indices]
it_seq_dim = [it_seq[i] for i in indices]

indices = (0, 1, 3, 6, 9)
time_seq_1000 = [time_seq_dim[i] for i in indices]
it_seq_1000 = [it_seq_dim[i] for i in indices]
indices = (2, 4, 7, 10)
time_seq_4000 = [time_seq_dim[i] for i in indices]
it_seq_4000 = [it_seq_dim[i] for i in indices]
indices = (5, 8, 11)
time_seq_10000 = [time_seq_dim[i] for i in indices]
it_seq_10000 = [it_seq_dim[i] for i in indices]

filename = "outputs/omp/RKAB.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_omp_1 = time[1::12]
time_omp_2 = time[3::12]
time_omp_4 = time[5::12]
time_omp_8 = time[7::12]
time_omp_16 = time[9::12]
time_omp_64 = time[11::12]

it_omp_1 = it[1::12]
it_omp_2 = it[3::12]
it_omp_4 = it[5::12]
it_omp_8 = it[7::12]
it_omp_16 = it[9::12]
it_omp_64 = it[11::12]

blocks = [5, 10, 100, 500, 1000, 2000, 4000, 10000]

lines_omp_2 = [it_omp_2[i]*2*blocks[i%8] for i in range(len(it_omp_2))]
lines_omp_4 = [it_omp_4[i]*4*blocks[i%8] for i in range(len(it_omp_4))]
lines_omp_8 = [it_omp_8[i]*8*blocks[i%8] for i in range(len(it_omp_8))]
lines_omp_16 = [it_omp_16[i]*16*blocks[i%8] for i in range(len(it_omp_16))]
lines_omp_64 = [it_omp_64[i]*64*blocks[i%8] for i in range(len(it_omp_64))]

filename = "outputs/omp/RKAB_dist.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_dist_1 = time[1::12]
time_dist_2 = time[3::12]
time_dist_4 = time[5::12]
time_dist_8 = time[7::12]
time_dist_16 = time[9::12]
time_dist_64 = time[11::12]

it_dist_1 = it[1::12]
it_dist_2 = it[3::12]
it_dist_4 = it[5::12]
it_dist_8 = it[7::12]
it_dist_16 = it[9::12]
it_dist_64 = it[11::12]

blocks = [5, 10, 100, 500, 1000, 2000, 4000, 10000]

lines_dist_2 = [it_dist_2[i]*2*blocks[i%8] for i in range(len(it_dist_2))]
lines_dist_4 = [it_dist_4[i]*4*blocks[i%8] for i in range(len(it_dist_4))]
lines_dist_8 = [it_dist_8[i]*8*blocks[i%8] for i in range(len(it_dist_8))]
lines_dist_16 = [it_dist_16[i]*16*blocks[i%8] for i in range(len(it_dist_16))]
lines_dist_64 = [it_dist_64[i]*64*blocks[i%8] for i in range(len(it_dist_64))]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'larger',
         'axes.titlesize':'larger',
         'xtick.labelsize': 'larger',
         'ytick.labelsize': 'larger'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = [5, 10, 100, 500, 1000, 2000, 4000, 10000]

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[5], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_omp_2[40:48], color='orange')
plt.plot(x, time_omp_2[40:48], linewidth=1.5, color='orange', label=r'Full Matrix Access (2 Threads)')
plt.scatter(x, time_omp_4[40:48], color='red')
plt.plot(x, time_omp_4[40:48], linewidth=1.5, color='red', label=r'Full Matrix Access (4 Threads)')
plt.scatter(x, time_omp_8[40:48], color='purple')
plt.plot(x, time_omp_8[40:48], linewidth=1.5, color='purple', label=r'Full Matrix Access (8 Threads)')
plt.scatter(x, time_omp_16[40:48], color='blue')
plt.plot(x, time_omp_16[40:48], linewidth=1.5, color='blue', label=r'Full Matrix Access (16 Threads)')
plt.scatter(x, time_omp_64[40:48], color='black')
plt.plot(x, time_omp_64[40:48], linewidth=1.5, color='black', label=r'Full Matrix Access (64 Threads)')
plt.scatter(x, time_dist_2, color='orange')
plt.plot(x, time_dist_2, linewidth=1.5, linestyle='--', color='orange', label=r'Distributed Approach (2 Threads)')
plt.scatter(x, time_dist_4, color='red')
plt.plot(x, time_dist_4, linewidth=1.5, linestyle='--', color='red', label=r'Distributed Approach (4 Threads)')
plt.scatter(x, time_dist_8, color='purple')
plt.plot(x, time_dist_8, linewidth=1.5, linestyle='--', color='purple', label=r'Distributed Approach (8 Threads)')
plt.scatter(x, time_dist_16, color='blue')
plt.plot(x, time_dist_16, linewidth=1.5, linestyle='--', color='blue', label=r'Distributed Approach (16 Threads)')
plt.scatter(x, time_dist_64, color='black')
plt.plot(x, time_dist_64, linewidth=1.5, linestyle='--', color='black', label=r'Distributed Approach (64 Threads)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_dist_comp_time_40000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[5], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, lines_omp_2[40:48], color='orange')
plt.plot(x, lines_omp_2[40:48], linewidth=1.5, color='orange', label=r'Full Matrix Access (2 Threads)')
plt.scatter(x, lines_omp_4[40:48], color='red')
plt.plot(x, lines_omp_4[40:48], linewidth=1.5, color='red', label=r'Full Matrix Access (4 Threads)')
plt.scatter(x, lines_omp_8[40:48], color='purple')
plt.plot(x, lines_omp_8[40:48], linewidth=1.5, color='purple', label=r'Full Matrix Access (8 Threads)')
plt.scatter(x, lines_omp_16[40:48], color='blue')
plt.plot(x, lines_omp_16[40:48], linewidth=1.5, color='blue', label=r'Full Matrix Access (16 Threads)')
plt.scatter(x, lines_omp_64[40:48], color='black')
plt.plot(x, lines_omp_64[40:48], linewidth=1.5, color='black', label=r'Full Matrix Access (64 Threads)')
plt.scatter(x, lines_dist_2, color='orange')
plt.plot(x, lines_dist_2, linewidth=1.5, linestyle='--', color='orange', label=r'Distributed Approach (2 Threads)')
plt.scatter(x, lines_dist_4, color='red')
plt.plot(x, lines_dist_4, linewidth=1.5, linestyle='--', color='red', label=r'Distributed Approach (4 Threads)')
plt.scatter(x, lines_dist_8, color='purple')
plt.plot(x, lines_dist_8, linewidth=1.5, linestyle='--', color='purple', label=r'Distributed Approach (8 Threads)')
plt.scatter(x, lines_dist_16, color='blue')
plt.plot(x, lines_dist_16, linewidth=1.5, linestyle='--', color='blue', label=r'Distributed Approach (16 Threads)')
plt.scatter(x, lines_dist_64, color='black')
plt.plot(x, lines_dist_64, linewidth=1.5, linestyle='--', color='black', label=r'Distributed Approach (64 Threads)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_dist_comp_lines_40000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[5], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, it_omp_2[40:48], color='orange')
plt.plot(x, it_omp_2[40:48], linewidth=1.5, color='orange', label=r'Full Matrix Access (2 Threads)')
plt.scatter(x, it_omp_4[40:48], color='red')
plt.plot(x, it_omp_4[40:48], linewidth=1.5, color='red', label=r'Full Matrix Access (4 Threads)')
plt.scatter(x, it_omp_8[40:48], color='purple')
plt.plot(x, it_omp_8[40:48], linewidth=1.5, color='purple', label=r'Full Matrix Access (8 Threads)')
plt.scatter(x, it_omp_16[40:48], color='blue')
plt.plot(x, it_omp_16[40:48], linewidth=1.5, color='blue', label=r'Full Matrix Access (16 Threads)')
plt.scatter(x, it_omp_64[40:48], color='black')
plt.plot(x, it_omp_64[40:48], linewidth=1.5, color='black', label=r'Full Matrix Access (64 Threads)')
plt.scatter(x, it_dist_2, color='orange')
plt.plot(x, it_dist_2, linewidth=1.5, linestyle='--', color='orange', label=r'Distributed Approach (2 Threads)')
plt.scatter(x, it_dist_4, color='red')
plt.plot(x, it_dist_4, linewidth=1.5, linestyle='--', color='red', label=r'Distributed Approach (4 Threads)')
plt.scatter(x, it_dist_8, color='purple')
plt.plot(x, it_dist_8, linewidth=1.5, linestyle='--', color='purple', label=r'Distributed Approach (8 Threads)')
plt.scatter(x, it_dist_16, color='blue')
plt.plot(x, it_dist_16, linewidth=1.5, linestyle='--', color='blue', label=r'Distributed Approach (16 Threads)')
plt.scatter(x, it_dist_64, color='black')
plt.plot(x, it_dist_64, linewidth=1.5, linestyle='--', color='black', label=r'Distributed Approach (64 Threads)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_dist_comp_it_40000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()