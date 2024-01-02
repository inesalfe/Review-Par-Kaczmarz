import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi/RKA_seq_alpha_comp.py

filename = "outputs/omp/navigator/RK.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(file_size):
    time_seq.append(float(lines[i].split()[2]))

indices = (10, 16, 18, 24, 26, 27, 33, 35, 36, 43, 45, 46)
time_seq_dim = [time_seq[i] for i in indices]

indices = (0, 1, 3, 6, 9)
time_seq_1000 = [time_seq_dim[i] for i in indices]
indices = (2, 4, 7, 10)
time_seq_4000 = [time_seq_dim[i] for i in indices]
indices = (5, 8, 11)
time_seq_10000 = [time_seq_dim[i] for i in indices]

filename = "outputs/mpi/navigator/RKA_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))

time_par_1 = time[1::14]
time_par_2 = time[3::14]
time_par_4 = time[5::14]
time_par_8 = time[7::14]
time_par_12 = time[9::14]
time_par_24 = time[11::14]
time_par_48 = time[13::14]

indices = (10, 16, 24, 33, 42)
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
time_par_12_1000 = [time_par_12[i] for i in indices]
time_par_24_1000 = [time_par_24[i] for i in indices]
time_par_48_1000 = [time_par_48[i] for i in indices]
speedup_2_1000 = [time_seq_1000[i]/time_par_2_1000[i] for i in range(len(indices))]
speedup_4_1000 = [time_seq_1000[i]/time_par_4_1000[i] for i in range(len(indices))]
speedup_8_1000 = [time_seq_1000[i]/time_par_8_1000[i] for i in range(len(indices))]
speedup_12_1000 = [time_seq_1000[i]/time_par_12_1000[i] for i in range(len(indices))]
speedup_24_1000 = [time_seq_1000[i]/time_par_24_1000[i] for i in range(len(indices))]
speedup_48_1000 = [time_seq_1000[i]/time_par_48_1000[i] for i in range(len(indices))]
x_1000 = [4000, 20000, 40000, 80000, 160000]

indices = (18, 26, 35, 44)
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
time_par_12_4000 = [time_par_12[i] for i in indices]
time_par_24_4000 = [time_par_24[i] for i in indices]
time_par_48_4000 = [time_par_48[i] for i in indices]
speedup_2_4000 = [time_seq_4000[i]/time_par_2_4000[i] for i in range(len(indices))]
speedup_4_4000 = [time_seq_4000[i]/time_par_4_4000[i] for i in range(len(indices))]
speedup_8_4000 = [time_seq_4000[i]/time_par_8_4000[i] for i in range(len(indices))]
speedup_12_4000 = [time_seq_4000[i]/time_par_12_4000[i] for i in range(len(indices))]
speedup_24_4000 = [time_seq_4000[i]/time_par_24_4000[i] for i in range(len(indices))]
speedup_48_4000 = [time_seq_4000[i]/time_par_48_4000[i] for i in range(len(indices))]
x_4000 = [20000, 40000, 80000, 160000]

indices = (27, 36, 45)
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
time_par_12_10000 = [time_par_12[i] for i in indices]
time_par_24_10000 = [time_par_24[i] for i in indices]
time_par_48_10000 = [time_par_48[i] for i in indices]
speedup_2_10000 = [time_seq_10000[i]/time_par_2_10000[i] for i in range(len(indices))]
speedup_4_10000 = [time_seq_10000[i]/time_par_4_10000[i] for i in range(len(indices))]
speedup_8_10000 = [time_seq_10000[i]/time_par_8_10000[i] for i in range(len(indices))]
speedup_12_10000 = [time_seq_10000[i]/time_par_12_10000[i] for i in range(len(indices))]
speedup_24_10000 = [time_seq_10000[i]/time_par_24_10000[i] for i in range(len(indices))]
speedup_48_10000 = [time_seq_10000[i]/time_par_48_10000[i] for i in range(len(indices))]
x_10000 = [40000, 80000, 160000]

filename = "outputs/mpi/navigator/RKA_alpha_2.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))

time_par_1 = time[0::7]
time_par_2 = time[1::7]
time_par_4 = time[2::7]
time_par_8 = time[3::7]
time_par_12 = time[4::7]
time_par_24 = time[5::7]
time_par_48 = time[6::7]

indices = (10, 16, 24, 33, 42)
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
time_par_12_1000 = [time_par_12[i] for i in indices]
time_par_24_1000 = [time_par_24[i] for i in indices]
time_par_48_1000 = [time_par_48[i] for i in indices]
speedup_2_1000_2 = [time_seq_1000[i]/time_par_2_1000[i] for i in range(len(indices))]
speedup_4_1000_2 = [time_seq_1000[i]/time_par_4_1000[i] for i in range(len(indices))]
speedup_8_1000_2 = [time_seq_1000[i]/time_par_8_1000[i] for i in range(len(indices))]
speedup_12_1000_2 = [time_seq_1000[i]/time_par_12_1000[i] for i in range(len(indices))]
speedup_24_1000_2 = [time_seq_1000[i]/time_par_24_1000[i] for i in range(len(indices))]
speedup_48_1000_2 = [time_seq_1000[i]/time_par_48_1000[i] for i in range(len(indices))]
x_1000 = [4000, 20000, 40000, 80000, 160000]

indices = (18, 26, 35, 44)
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
time_par_12_4000 = [time_par_12[i] for i in indices]
time_par_24_4000 = [time_par_24[i] for i in indices]
time_par_48_4000 = [time_par_48[i] for i in indices]
speedup_2_4000_2 = [time_seq_4000[i]/time_par_2_4000[i] for i in range(len(indices))]
speedup_4_4000_2 = [time_seq_4000[i]/time_par_4_4000[i] for i in range(len(indices))]
speedup_8_4000_2 = [time_seq_4000[i]/time_par_8_4000[i] for i in range(len(indices))]
speedup_12_4000_2 = [time_seq_4000[i]/time_par_12_4000[i] for i in range(len(indices))]
speedup_24_4000_2 = [time_seq_4000[i]/time_par_24_4000[i] for i in range(len(indices))]
speedup_48_4000_2 = [time_seq_4000[i]/time_par_48_4000[i] for i in range(len(indices))]
x_4000 = [20000, 40000, 80000, 160000]

indices = (27, 36, 45)
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
time_par_12_10000 = [time_par_12[i] for i in indices]
time_par_24_10000 = [time_par_24[i] for i in indices]
time_par_48_10000 = [time_par_48[i] for i in indices]
speedup_2_10000_2 = [time_seq_10000[i]/time_par_2_10000[i] for i in range(len(indices))]
speedup_4_10000_2 = [time_seq_10000[i]/time_par_4_10000[i] for i in range(len(indices))]
speedup_8_10000_2 = [time_seq_10000[i]/time_par_8_10000[i] for i in range(len(indices))]
speedup_12_10000_2 = [time_seq_10000[i]/time_par_12_10000[i] for i in range(len(indices))]
speedup_24_10000_2 = [time_seq_10000[i]/time_par_24_10000[i] for i in range(len(indices))]
speedup_48_10000_2 = [time_seq_10000[i]/time_par_48_10000[i] for i in range(len(indices))]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'larger',
         'axes.titlesize': 'larger',
         'xtick.labelsize': 'larger',
         'ytick.labelsize': 'larger'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(12, 9))
plt.scatter(x_1000, speedup_2_1000, color='yellow')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x_1000, speedup_4_1000, color='orange')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='orange', label=r'4')
plt.scatter(x_1000, speedup_8_1000, color='red')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='red', label=r'8')
plt.scatter(x_1000, speedup_12_1000, color='blue')
plt.plot(x_1000, speedup_12_1000, linewidth=1.5, color='blue', label=r'12')
plt.scatter(x_1000, speedup_24_1000, color='purple')
plt.plot(x_1000, speedup_24_1000, linewidth=1.5, color='purple', label=r'24')
plt.scatter(x_1000, speedup_48_1000, color='black')
plt.plot(x_1000, speedup_48_1000, linewidth=1.5, color='black', label=r'48')
plt.scatter(x_1000, speedup_2_1000_2, color='yellow')
plt.plot(x_1000, speedup_2_1000_2, linewidth=1.5, linestyle='--', color='yellow', label=r'2 (2 processes / node)')
plt.scatter(x_1000, speedup_4_1000_2, color='orange')
plt.plot(x_1000, speedup_4_1000_2, linewidth=1.5, linestyle='--', color='orange', label=r'4 (2 processes / node)')
plt.scatter(x_1000, speedup_8_1000_2, color='red')
plt.plot(x_1000, speedup_8_1000_2, linewidth=1.5, linestyle='--', color='red', label=r'8 (2 processes / node)')
plt.scatter(x_1000, speedup_12_1000, color='blue')
plt.plot(x_1000, speedup_12_1000_2, linewidth=1.5, linestyle='--', color='blue', label=r'12 (2 processes / node)')
plt.scatter(x_1000, speedup_24_1000_2, color='purple')
plt.plot(x_1000, speedup_24_1000_2, linewidth=1.5, linestyle='--', color='purple', label=r'24 (2 processes / node)')
plt.scatter(x_1000, speedup_48_1000_2, color='black')
plt.plot(x_1000, speedup_48_1000_2, linewidth=1.5, linestyle='--', color='black', label=r'48 (2 processes / node)')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_alpha_comp_speedup_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(12, 9))
plt.scatter(x_4000, speedup_2_4000, color='yellow')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x_4000, speedup_4_4000, color='orange')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='orange', label=r'4')
plt.scatter(x_4000, speedup_8_4000, color='red')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='red', label=r'8')
plt.scatter(x_4000, speedup_12_4000, color='blue')
plt.plot(x_4000, speedup_12_4000, linewidth=1.5, color='blue', label=r'12')
plt.scatter(x_4000, speedup_24_4000, color='purple')
plt.plot(x_4000, speedup_24_4000, linewidth=1.5, color='purple', label=r'24')
plt.scatter(x_4000, speedup_48_4000, color='black')
plt.plot(x_4000, speedup_48_4000, linewidth=1.5, color='black', label=r'48')
plt.scatter(x_4000, speedup_2_4000_2, color='yellow')
plt.plot(x_4000, speedup_2_4000_2, linewidth=1.5, linestyle='--', color='yellow', label=r'2 (2 processes / node)')
plt.scatter(x_4000, speedup_4_4000_2, color='orange')
plt.plot(x_4000, speedup_4_4000_2, linewidth=1.5, linestyle='--', color='orange', label=r'4 (2 processes / node)')
plt.scatter(x_4000, speedup_8_4000_2, color='red')
plt.plot(x_4000, speedup_8_4000_2, linewidth=1.5, linestyle='--', color='red', label=r'8 (2 processes / node)')
plt.scatter(x_4000, speedup_12_4000, color='blue')
plt.plot(x_4000, speedup_12_4000_2, linewidth=1.5, linestyle='--', color='blue', label=r'12 (2 processes / node)')
plt.scatter(x_4000, speedup_24_4000_2, color='purple')
plt.plot(x_4000, speedup_24_4000_2, linewidth=1.5, linestyle='--', color='purple', label=r'24 (2 processes / node)')
plt.scatter(x_4000, speedup_48_4000_2, color='black')
plt.plot(x_4000, speedup_48_4000_2, linewidth=1.5, linestyle='--', color='black', label=r'48 (2 processes / node)')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_alpha_comp_speedup_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(12, 9))
plt.scatter(x_10000, speedup_2_10000, color='yellow')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x_10000, speedup_4_10000, color='orange')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='orange', label=r'4')
plt.scatter(x_10000, speedup_8_10000, color='red')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='red', label=r'8')
plt.scatter(x_10000, speedup_12_10000, color='blue')
plt.plot(x_10000, speedup_12_10000, linewidth=1.5, color='blue', label=r'12')
plt.scatter(x_10000, speedup_24_10000, color='purple')
plt.plot(x_10000, speedup_24_10000, linewidth=1.5, color='purple', label=r'24')
plt.scatter(x_10000, speedup_48_10000, color='black')
plt.plot(x_10000, speedup_48_10000, linewidth=1.5, color='black', label=r'48')
plt.scatter(x_10000, speedup_2_10000_2, color='yellow')
plt.plot(x_10000, speedup_2_10000_2, linewidth=1.5, linestyle='--', color='yellow', label=r'2 (2 processes / node)')
plt.scatter(x_10000, speedup_4_10000_2, color='orange')
plt.plot(x_10000, speedup_4_10000_2, linewidth=1.5, linestyle='--', color='orange', label=r'4 (2 processes / node)')
plt.scatter(x_10000, speedup_8_10000_2, color='red')
plt.plot(x_10000, speedup_8_10000_2, linewidth=1.5, linestyle='--', color='red', label=r'8 (2 processes / node)')
plt.scatter(x_10000, speedup_12_10000, color='blue')
plt.plot(x_10000, speedup_12_10000_2, linewidth=1.5, linestyle='--', color='blue', label=r'12 (2 processes / node)')
plt.scatter(x_10000, speedup_24_10000_2, color='purple')
plt.plot(x_10000, speedup_24_10000_2, linewidth=1.5, linestyle='--', color='purple', label=r'24 (2 processes / node)')
plt.scatter(x_10000, speedup_48_10000_2, color='black')
plt.plot(x_10000, speedup_48_10000_2, linewidth=1.5, linestyle='--', color='black', label=r'48 (2 processes / node)')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_alpha_comp_speedup_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()