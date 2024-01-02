import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi/RKAB_comp.py

filename = "outputs/omp/navigator/RK.txt";

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

filename = "outputs/mpi/navigator/RKAB.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_mpi_1_1 = time[1::14]
time_mpi_1_2 = time[3::14]
time_mpi_1_4 = time[5::14]
time_mpi_1_8 = time[7::14]
time_mpi_1_12 = time[9::14]
time_mpi_1_24 = time[11::14]
time_mpi_1_48 = time[13::14]

filename = "outputs/mpi/navigator/RKAB_2.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_mpi_2_1 = time[0::7]
time_mpi_2_2 = time[1::7]
time_mpi_2_4 = time[2::7]
time_mpi_2_8 = time[3::7]
time_mpi_2_12 = time[4::7]
time_mpi_2_24 = time[5::7]
time_mpi_2_48 = time[6::7]

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

plot_title = r"$4000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[0], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[0:8], color='yellow')
plt.plot(x, time_mpi_1_2[0:8], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[0:8], color='orange')
plt.plot(x, time_mpi_1_4[0:8], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[0:8], color='red')
plt.plot(x, time_mpi_1_8[0:8], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[0:8], color='purple')
plt.plot(x, time_mpi_1_12[0:8], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[0:8], color='blue')
plt.plot(x, time_mpi_1_24[0:8], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[0:8], color='black')
plt.plot(x, time_mpi_1_48[0:8], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[0:8], color='yellow')
plt.plot(x, time_mpi_2_2[0:8], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[0:8], color='orange')
plt.plot(x, time_mpi_2_4[0:8], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[0:8], color='red')
plt.plot(x, time_mpi_2_8[0:8], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[0:8], color='purple')
plt.plot(x, time_mpi_2_12[0:8], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[0:8], color='blue')
plt.plot(x, time_mpi_2_24[0:8], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[0:8], color='black')
plt.plot(x, time_mpi_2_48[0:8], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_4000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$20000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[1], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[8:16], color='yellow')
plt.plot(x, time_mpi_1_2[8:16], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[8:16], color='orange')
plt.plot(x, time_mpi_1_4[8:16], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[8:16], color='red')
plt.plot(x, time_mpi_1_8[8:16], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[8:16], color='purple')
plt.plot(x, time_mpi_1_12[8:16], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[8:16], color='blue')
plt.plot(x, time_mpi_1_24[8:16], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[8:16], color='black')
plt.plot(x, time_mpi_1_48[8:16], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[8:16], color='yellow')
plt.plot(x, time_mpi_2_2[8:16], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[8:16], color='orange')
plt.plot(x, time_mpi_2_4[8:16], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[8:16], color='red')
plt.plot(x, time_mpi_2_8[8:16], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[8:16], color='purple')
plt.plot(x, time_mpi_2_12[8:16], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[8:16], color='blue')
plt.plot(x, time_mpi_2_24[8:16], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[8:16], color='black')
plt.plot(x, time_mpi_2_48[8:16], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_20000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$20000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[2], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[16:24], color='yellow')
plt.plot(x, time_mpi_1_2[16:24], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[16:24], color='orange')
plt.plot(x, time_mpi_1_4[16:24], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[16:24], color='red')
plt.plot(x, time_mpi_1_8[16:24], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[16:24], color='purple')
plt.plot(x, time_mpi_1_12[16:24], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[16:24], color='blue')
plt.plot(x, time_mpi_1_24[16:24], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[16:24], color='black')
plt.plot(x, time_mpi_1_48[16:24], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[16:24], color='yellow')
plt.plot(x, time_mpi_2_2[16:24], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[16:24], color='orange')
plt.plot(x, time_mpi_2_4[16:24], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[16:24], color='red')
plt.plot(x, time_mpi_2_8[16:24], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[16:24], color='purple')
plt.plot(x, time_mpi_2_12[16:24], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[16:24], color='blue')
plt.plot(x, time_mpi_2_24[16:24], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[16:24], color='black')
plt.plot(x, time_mpi_2_48[16:24], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_20000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[3], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[24:32], color='yellow')
plt.plot(x, time_mpi_1_2[24:32], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[24:32], color='orange')
plt.plot(x, time_mpi_1_4[24:32], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[24:32], color='red')
plt.plot(x, time_mpi_1_8[24:32], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[24:32], color='purple')
plt.plot(x, time_mpi_1_12[24:32], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[24:32], color='blue')
plt.plot(x, time_mpi_1_24[24:32], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[24:32], color='black')
plt.plot(x, time_mpi_1_48[24:32], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[24:32], color='yellow')
plt.plot(x, time_mpi_2_2[24:32], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[24:32], color='orange')
plt.plot(x, time_mpi_2_4[24:32], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[24:32], color='red')
plt.plot(x, time_mpi_2_8[24:32], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[24:32], color='purple')
plt.plot(x, time_mpi_2_12[24:32], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[24:32], color='blue')
plt.plot(x, time_mpi_2_24[24:32], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[24:32], color='black')
plt.plot(x, time_mpi_2_48[24:32], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_40000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[4], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[32:40], color='yellow')
plt.plot(x, time_mpi_1_2[32:40], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[32:40], color='orange')
plt.plot(x, time_mpi_1_4[32:40], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[32:40], color='red')
plt.plot(x, time_mpi_1_8[32:40], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[32:40], color='purple')
plt.plot(x, time_mpi_1_12[32:40], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[32:40], color='blue')
plt.plot(x, time_mpi_1_24[32:40], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[32:40], color='black')
plt.plot(x, time_mpi_1_48[32:40], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[32:40], color='yellow')
plt.plot(x, time_mpi_2_2[32:40], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[32:40], color='orange')
plt.plot(x, time_mpi_2_4[32:40], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[32:40], color='red')
plt.plot(x, time_mpi_2_8[32:40], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[32:40], color='purple')
plt.plot(x, time_mpi_2_12[32:40], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[32:40], color='blue')
plt.plot(x, time_mpi_2_24[32:40], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[32:40], color='black')
plt.plot(x, time_mpi_2_48[32:40], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_40000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[5], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[40:48], color='yellow')
plt.plot(x, time_mpi_1_2[40:48], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[40:48], color='orange')
plt.plot(x, time_mpi_1_4[40:48], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[40:48], color='red')
plt.plot(x, time_mpi_1_8[40:48], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[40:48], color='purple')
plt.plot(x, time_mpi_1_12[40:48], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[40:48], color='blue')
plt.plot(x, time_mpi_1_24[40:48], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[40:48], color='black')
plt.plot(x, time_mpi_1_48[40:48], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[40:48], color='yellow')
plt.plot(x, time_mpi_2_2[40:48], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[40:48], color='orange')
plt.plot(x, time_mpi_2_4[40:48], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[40:48], color='red')
plt.plot(x, time_mpi_2_8[40:48], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[40:48], color='purple')
plt.plot(x, time_mpi_2_12[40:48], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[40:48], color='blue')
plt.plot(x, time_mpi_2_24[40:48], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[40:48], color='black')
plt.plot(x, time_mpi_2_48[40:48], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_40000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[6], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[48:56], color='yellow')
plt.plot(x, time_mpi_1_2[48:56], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[48:56], color='orange')
plt.plot(x, time_mpi_1_4[48:56], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[48:56], color='red')
plt.plot(x, time_mpi_1_8[48:56], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[48:56], color='purple')
plt.plot(x, time_mpi_1_12[48:56], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[48:56], color='blue')
plt.plot(x, time_mpi_1_24[48:56], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[48:56], color='black')
plt.plot(x, time_mpi_1_48[48:56], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[48:56], color='yellow')
plt.plot(x, time_mpi_2_2[48:56], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[48:56], color='orange')
plt.plot(x, time_mpi_2_4[48:56], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[48:56], color='red')
plt.plot(x, time_mpi_2_8[48:56], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[48:56], color='purple')
plt.plot(x, time_mpi_2_12[48:56], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[48:56], color='blue')
plt.plot(x, time_mpi_2_24[48:56], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[48:56], color='black')
plt.plot(x, time_mpi_2_48[48:56], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_80000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[7], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[56:64], color='yellow')
plt.plot(x, time_mpi_1_2[56:64], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[56:64], color='orange')
plt.plot(x, time_mpi_1_4[56:64], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[56:64], color='red')
plt.plot(x, time_mpi_1_8[56:64], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[56:64], color='purple')
plt.plot(x, time_mpi_1_12[56:64], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[56:64], color='blue')
plt.plot(x, time_mpi_1_24[56:64], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[56:64], color='black')
plt.plot(x, time_mpi_1_48[56:64], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[56:64], color='yellow')
plt.plot(x, time_mpi_2_2[56:64], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[56:64], color='orange')
plt.plot(x, time_mpi_2_4[56:64], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[56:64], color='red')
plt.plot(x, time_mpi_2_8[56:64], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[56:64], color='purple')
plt.plot(x, time_mpi_2_12[56:64], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[56:64], color='blue')
plt.plot(x, time_mpi_2_24[56:64], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[56:64], color='black')
plt.plot(x, time_mpi_2_48[56:64], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_80000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[8], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[64:72], color='yellow')
plt.plot(x, time_mpi_1_2[64:72], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[64:72], color='orange')
plt.plot(x, time_mpi_1_4[64:72], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[64:72], color='red')
plt.plot(x, time_mpi_1_8[64:72], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[64:72], color='purple')
plt.plot(x, time_mpi_1_12[64:72], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[64:72], color='blue')
plt.plot(x, time_mpi_1_24[64:72], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[64:72], color='black')
plt.plot(x, time_mpi_1_48[64:72], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[64:72], color='yellow')
plt.plot(x, time_mpi_2_2[64:72], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[64:72], color='orange')
plt.plot(x, time_mpi_2_4[64:72], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[64:72], color='red')
plt.plot(x, time_mpi_2_8[64:72], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[64:72], color='purple')
plt.plot(x, time_mpi_2_12[64:72], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[64:72], color='blue')
plt.plot(x, time_mpi_2_24[64:72], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[64:72], color='black')
plt.plot(x, time_mpi_2_48[64:72], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_80000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$160000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[9], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[72:80], color='yellow')
plt.plot(x, time_mpi_1_2[72:80], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[72:80], color='orange')
plt.plot(x, time_mpi_1_4[72:80], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[72:80], color='red')
plt.plot(x, time_mpi_1_8[72:80], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[72:80], color='purple')
plt.plot(x, time_mpi_1_12[72:80], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[72:80], color='blue')
plt.plot(x, time_mpi_1_24[72:80], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[72:80], color='black')
plt.plot(x, time_mpi_1_48[72:80], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[72:80], color='yellow')
plt.plot(x, time_mpi_2_2[72:80], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[72:80], color='orange')
plt.plot(x, time_mpi_2_4[72:80], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[72:80], color='red')
plt.plot(x, time_mpi_2_8[72:80], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[72:80], color='purple')
plt.plot(x, time_mpi_2_12[72:80], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[72:80], color='blue')
plt.plot(x, time_mpi_2_24[72:80], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[72:80], color='black')
plt.plot(x, time_mpi_2_48[72:80], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_160000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$160000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[10], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[80:88], color='yellow')
plt.plot(x, time_mpi_1_2[80:88], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[80:88], color='orange')
plt.plot(x, time_mpi_1_4[80:88], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[80:88], color='red')
plt.plot(x, time_mpi_1_8[80:88], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[80:88], color='purple')
plt.plot(x, time_mpi_1_12[80:88], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[80:88], color='blue')
plt.plot(x, time_mpi_1_24[80:88], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[80:88], color='black')
plt.plot(x, time_mpi_1_48[80:88], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[80:88], color='yellow')
plt.plot(x, time_mpi_2_2[80:88], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[80:88], color='orange')
plt.plot(x, time_mpi_2_4[80:88], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[80:88], color='red')
plt.plot(x, time_mpi_2_8[80:88], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[80:88], color='purple')
plt.plot(x, time_mpi_2_12[80:88], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[80:88], color='blue')
plt.plot(x, time_mpi_2_24[80:88], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[80:88], color='black')
plt.plot(x, time_mpi_2_48[80:88], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_160000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$160000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[11], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x, time_mpi_1_2[88:96], color='yellow')
plt.plot(x, time_mpi_1_2[88:96], linewidth=1.5, color='yellow', label=r'2')
plt.scatter(x, time_mpi_1_4[88:96], color='orange')
plt.plot(x, time_mpi_1_4[88:96], linewidth=1.5, color='orange', label=r'4')
plt.scatter(x, time_mpi_1_8[88:96], color='red')
plt.plot(x, time_mpi_1_8[88:96], linewidth=1.5, color='red', label=r'8')
plt.scatter(x, time_mpi_1_12[88:96], color='purple')
plt.plot(x, time_mpi_1_12[88:96], linewidth=1.5, color='purple', label=r'12')
plt.scatter(x, time_mpi_1_24[88:96], color='blue')
plt.plot(x, time_mpi_1_24[88:96], linewidth=1.5, color='blue', label=r'24')
plt.scatter(x, time_mpi_1_48[88:96], color='black')
plt.plot(x, time_mpi_1_48[88:96], linewidth=1.5, color='black', label=r'48')
plt.scatter(x, time_mpi_2_2[88:96], color='yellow')
plt.plot(x, time_mpi_2_2[88:96], linestyle='--', linewidth=1.5, color='yellow', label=r'2 (2 processes/node)')
plt.scatter(x, time_mpi_2_4[88:96], color='orange')
plt.plot(x, time_mpi_2_4[88:96], linestyle='--', linewidth=1.5, color='orange', label=r'4 (2 processes/node)')
plt.scatter(x, time_mpi_2_8[88:96], color='red')
plt.plot(x, time_mpi_2_8[88:96], linestyle='--', linewidth=1.5, color='red', label=r'8 (2 processes/node)')
plt.scatter(x, time_mpi_2_12[88:96], color='purple')
plt.plot(x, time_mpi_2_12[88:96], linestyle='--', linewidth=1.5, color='purple', label=r'12 (2 processes/node)')
plt.scatter(x, time_mpi_2_24[88:96], color='blue')
plt.plot(x, time_mpi_2_24[88:96], linestyle='--', linewidth=1.5, color='blue', label=r'24 (2 processes/node)')
plt.scatter(x, time_mpi_2_48[88:96], color='black')
plt.plot(x, time_mpi_2_48[88:96], linestyle='--', linewidth=1.5, color='black', label=r'48 (2 processes/node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_comp_time_160000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()