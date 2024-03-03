import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/madrid/RKA_seq_N.py

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
time_seq = [time_seq[i] for i in indices]
it_seq = [it_seq[i] for i in indices]

indices = (0, 1, 3, 6, 9)
time_seq_1000 = [time_seq[i] for i in indices]
it_seq_1000 = [it_seq[i] for i in indices]
indices = (2, 4, 7, 10)
time_seq_4000 = [time_seq[i] for i in indices]
it_seq_4000 = [it_seq[i] for i in indices]
indices = (5, 8, 11)
time_seq_10000 = [time_seq[i] for i in indices]
it_seq_10000 = [it_seq[i] for i in indices]

filename = "outputs/omp/RKA.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(float(lines[i].split()[3]))

it_seq_1 = it[0::12]
it_seq_2 = it[2::12]
it_seq_4 = it[4::12]
it_seq_8 = it[6::12]
it_seq_16 = it[8::12]
it_seq_64 = it[10::12]

it_par_1 = it[1::12]
it_par_2 = it[3::12]
it_par_4 = it[5::12]
it_par_8 = it[7::12]
it_par_16 = it[9::12]
it_par_64 = it[11::12]

time_seq_1 = time[0::12]
time_seq_2 = time[2::12]
time_seq_4 = time[4::12]
time_seq_8 = time[6::12]
time_seq_16 = time[8::12]
time_seq_64 = time[10::12]

time_par_1 = time[1::12]
time_par_2 = time[3::12]
time_par_4 = time[5::12]
time_par_8 = time[7::12]
time_par_16 = time[9::12]
time_par_64 = time[11::12]

indices = (10, 16, 24, 33, 42)
it_seq_1_1000 = [it_seq_1[i] for i in indices]
it_seq_2_1000 = [it_seq_2[i] for i in indices]
it_seq_4_1000 = [it_seq_4[i] for i in indices]
it_seq_8_1000 = [it_seq_8[i] for i in indices]
it_seq_16_1000 = [it_seq_16[i] for i in indices]
it_seq_64_1000 = [it_seq_64[i] for i in indices]
time_seq_1_1000 = [time_seq_1[i] for i in indices]
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
time_seq_16_1000 = [time_seq_16[i] for i in indices]
time_seq_64_1000 = [time_seq_64[i] for i in indices]
it_par_1_1000 = [it_par_1[i] for i in indices]
it_par_2_1000 = [it_par_2[i] for i in indices]
it_par_4_1000 = [it_par_4[i] for i in indices]
it_par_8_1000 = [it_par_8[i] for i in indices]
it_par_16_1000 = [it_par_16[i] for i in indices]
it_par_64_1000 = [it_par_64[i] for i in indices]
total_lines_par_1_1000 = [it_par_1[i] for i in indices]
total_lines_par_2_1000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_1000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_1000 = [8*it_par_8[i] for i in indices]
total_lines_par_16_1000 = [16*it_par_16[i] for i in indices]
total_lines_par_64_1000 = [64*it_par_64[i] for i in indices]
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
time_par_16_1000 = [time_par_16[i] for i in indices]
time_par_64_1000 = [time_par_64[i] for i in indices]
speedup_2_1000 = [time_seq_1000[i]/time_par_2_1000[i] for i in range(len(indices))]
speedup_4_1000 = [time_seq_1000[i]/time_par_4_1000[i] for i in range(len(indices))]
speedup_8_1000 = [time_seq_1000[i]/time_par_8_1000[i] for i in range(len(indices))]
speedup_16_1000 = [time_seq_1000[i]/time_par_16_1000[i] for i in range(len(indices))]
speedup_64_1000 = [time_seq_1000[i]/time_par_64_1000[i] for i in range(len(indices))]
x_1000 = [4000, 20000, 40000, 80000, 160000]

indices = (18, 26, 35, 44)
it_seq_1_4000 = [it_seq_1[i] for i in indices]
it_seq_2_4000 = [it_seq_2[i] for i in indices]
it_seq_4_4000 = [it_seq_4[i] for i in indices]
it_seq_8_4000 = [it_seq_8[i] for i in indices]
it_seq_16_4000 = [it_seq_16[i] for i in indices]
it_seq_64_4000 = [it_seq_64[i] for i in indices]
time_seq_1_4000 = [time_seq_1[i] for i in indices]
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
time_seq_16_4000 = [time_seq_16[i] for i in indices]
time_seq_64_4000 = [time_seq_64[i] for i in indices]
it_par_1_4000 = [it_par_1[i] for i in indices]
it_par_2_4000 = [it_par_2[i] for i in indices]
it_par_4_4000 = [it_par_4[i] for i in indices]
it_par_8_4000 = [it_par_8[i] for i in indices]
it_par_16_4000 = [it_par_16[i] for i in indices]
it_par_64_4000 = [it_par_64[i] for i in indices]
total_lines_par_1_4000 = [it_par_1[i] for i in indices]
total_lines_par_2_4000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_4000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_4000 = [8*it_par_8[i] for i in indices]
total_lines_par_16_4000 = [16*it_par_16[i] for i in indices]
total_lines_par_64_4000 = [64*it_par_64[i] for i in indices]
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
time_par_16_4000 = [time_par_16[i] for i in indices]
time_par_64_4000 = [time_par_64[i] for i in indices]
speedup_2_4000 = [time_seq_4000[i]/time_par_2_4000[i] for i in range(len(indices))]
speedup_4_4000 = [time_seq_4000[i]/time_par_4_4000[i] for i in range(len(indices))]
speedup_8_4000 = [time_seq_4000[i]/time_par_8_4000[i] for i in range(len(indices))]
speedup_16_4000 = [time_seq_4000[i]/time_par_16_4000[i] for i in range(len(indices))]
speedup_64_4000 = [time_seq_4000[i]/time_par_64_4000[i] for i in range(len(indices))]
x_4000 = [20000, 40000, 80000, 160000]

indices = (27, 36, 45)
it_seq_1_10000 = [it_seq_1[i] for i in indices]
it_seq_2_10000 = [it_seq_2[i] for i in indices]
it_seq_4_10000 = [it_seq_4[i] for i in indices]
it_seq_8_10000 = [it_seq_8[i] for i in indices]
it_seq_16_10000 = [it_seq_16[i] for i in indices]
it_seq_64_10000 = [it_seq_64[i] for i in indices]
time_seq_1_10000 = [time_seq_1[i] for i in indices]
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
time_seq_16_10000 = [time_seq_16[i] for i in indices]
time_seq_64_10000 = [time_seq_64[i] for i in indices]
it_par_1_10000 = [it_par_1[i] for i in indices]
it_par_2_10000 = [it_par_2[i] for i in indices]
it_par_4_10000 = [it_par_4[i] for i in indices]
it_par_8_10000 = [it_par_8[i] for i in indices]
it_par_16_10000 = [it_par_16[i] for i in indices]
it_par_64_10000 = [it_par_64[i] for i in indices]
total_lines_par_1_10000 = [it_par_1[i] for i in indices]
total_lines_par_2_10000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_10000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_10000 = [8*it_par_8[i] for i in indices]
total_lines_par_16_10000 = [16*it_par_16[i] for i in indices]
total_lines_par_64_10000 = [64*it_par_64[i] for i in indices]
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
time_par_16_10000 = [time_par_16[i] for i in indices]
time_par_64_10000 = [time_par_64[i] for i in indices]
speedup_2_10000 = [time_seq_10000[i]/time_par_2_10000[i] for i in range(len(indices))]
speedup_4_10000 = [time_seq_10000[i]/time_par_4_10000[i] for i in range(len(indices))]
speedup_8_10000 = [time_seq_10000[i]/time_par_8_10000[i] for i in range(len(indices))]
speedup_16_10000 = [time_seq_10000[i]/time_par_16_10000[i] for i in range(len(indices))]
speedup_64_10000 = [time_seq_10000[i]/time_par_64_10000[i] for i in range(len(indices))]
x_10000 = [40000, 80000, 160000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, total_lines_par_2_1000, color='orange')
plt.plot(x_1000, total_lines_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 2 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, total_lines_par_2_4000, color='red')
plt.plot(x_4000, total_lines_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 2 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, total_lines_par_2_10000, color='blue')
plt.plot(x_10000, total_lines_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 2 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_2"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, total_lines_par_4_1000, color='orange')
plt.plot(x_1000, total_lines_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 4 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, total_lines_par_4_4000, color='red')
plt.plot(x_4000, total_lines_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 4 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, total_lines_par_4_10000, color='blue')
plt.plot(x_10000, total_lines_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 4 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_4"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, total_lines_par_8_1000, color='orange')
plt.plot(x_1000, total_lines_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 8 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, total_lines_par_8_4000, color='red')
plt.plot(x_4000, total_lines_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 8 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, total_lines_par_8_10000, color='blue')
plt.plot(x_10000, total_lines_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 8 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_8"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, total_lines_par_16_1000, color='orange')
plt.plot(x_1000, total_lines_par_16_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 16 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, total_lines_par_16_4000, color='red')
plt.plot(x_4000, total_lines_par_16_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 16 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, total_lines_par_16_10000, color='blue')
plt.plot(x_10000, total_lines_par_16_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 16 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_16"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, total_lines_par_64_1000, color='orange')
plt.plot(x_1000, total_lines_par_64_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 64 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, total_lines_par_64_4000, color='red')
plt.plot(x_4000, total_lines_par_64_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 64 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, total_lines_par_64_10000, color='blue')
plt.plot(x_10000, total_lines_par_64_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 64 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_64"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 2 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_par_2_4000, color='red')
plt.plot(x_4000, it_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 2 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_par_2_10000, color='blue')
plt.plot(x_10000, it_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 2 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_2"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, it_par_4_1000, color='orange')
plt.plot(x_1000, it_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 4 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_par_4_4000, color='red')
plt.plot(x_4000, it_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 4 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_par_4_10000, color='blue')
plt.plot(x_10000, it_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 4 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_4"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, it_par_8_1000, color='orange')
plt.plot(x_1000, it_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 8 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_par_8_4000, color='red')
plt.plot(x_4000, it_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 8 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_par_8_10000, color='blue')
plt.plot(x_10000, it_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 8 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_8"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, it_par_16_1000, color='orange')
plt.plot(x_1000, it_par_16_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 16 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_par_16_4000, color='red')
plt.plot(x_4000, it_par_16_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 16 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_par_16_10000, color='blue')
plt.plot(x_10000, it_par_16_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 16 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_16"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, it_par_64_1000, color='orange')
plt.plot(x_1000, it_par_64_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 64 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, it_par_64_4000, color='red')
plt.plot(x_4000, it_par_64_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 64 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, it_par_64_10000, color='blue')
plt.plot(x_10000, it_par_64_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 64 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_64"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 2 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_par_2_4000, color='red')
plt.plot(x_4000, time_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 2 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 2 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_2"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, time_par_4_1000, color='orange')
plt.plot(x_1000, time_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 4 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 4 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 4 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_4"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, time_par_8_1000, color='orange')
plt.plot(x_1000, time_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 8 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_par_8_4000, color='red')
plt.plot(x_4000, time_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 8 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 8 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_8"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, time_par_16_1000, color='orange')
plt.plot(x_1000, time_par_16_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 16 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_par_16_4000, color='red')
plt.plot(x_4000, time_par_16_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 16 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_par_16_10000, color='blue')
plt.plot(x_10000, time_par_16_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 16 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_16"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$', marker='X', markersize=10)
# plt.scatter(x_1000, time_par_64_1000, color='orange')
plt.plot(x_1000, time_par_64_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 64 Threads - $n = 1000$', marker='s', markersize=10)
# plt.scatter(x_4000, time_par_64_4000, color='red')
plt.plot(x_4000, time_par_64_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 64 Threads - $n = 4000$', marker='o', markersize=10)
# plt.scatter(x_10000, time_par_64_10000, color='blue')
plt.plot(x_10000, time_par_64_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 64 Threads - $n = 10000$', marker='X', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_64"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='gray')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_1000, total_lines_par_2_1000, color='orange')
plt.plot(x_1000, total_lines_par_2_1000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_1000, total_lines_par_4_1000, color='red')
plt.plot(x_1000, total_lines_par_4_1000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_1000, total_lines_par_8_1000, color='purple')
plt.plot(x_1000, total_lines_par_8_1000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_1000, total_lines_par_16_1000, color='blue')
plt.plot(x_1000, total_lines_par_16_1000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_1000, total_lines_par_64_1000, color='black')
plt.plot(x_1000, total_lines_par_64_1000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_1000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, it_seq_1000, color='gray')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_1000, it_par_4_1000, color='red')
plt.plot(x_1000, it_par_4_1000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_1000, it_par_8_1000, color='purple')
plt.plot(x_1000, it_par_8_1000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_1000, it_par_16_1000, color='blue')
plt.plot(x_1000, it_par_16_1000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_1000, it_par_64_1000, color='black')
plt.plot(x_1000, it_par_64_1000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_1000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, time_seq_1000, color='gray')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_1000, time_par_4_1000, color='red')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_1000, time_par_8_1000, color='purple')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_1000, time_par_16_1000, color='blue')
plt.plot(x_1000, time_par_16_1000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_1000, time_par_64_1000, color='black')
plt.plot(x_1000, time_par_64_1000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_1000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_1000, speedup_4_1000, color='red')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='red', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_1000, speedup_8_1000, color='purple')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='purple', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_1000, speedup_16_1000, color='blue')
plt.plot(x_1000, speedup_16_1000, linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_1000, speedup_64_1000, color='black')
plt.plot(x_1000, speedup_64_1000, linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_N_speedup_1000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_4000, it_seq_4000, color='gray')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_4000, total_lines_par_2_4000, color='orange')
plt.plot(x_4000, total_lines_par_2_4000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_4000, total_lines_par_4_4000, color='red')
plt.plot(x_4000, total_lines_par_4_4000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_4000, total_lines_par_8_4000, color='purple')
plt.plot(x_4000, total_lines_par_8_4000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_4000, total_lines_par_16_4000, color='blue')
plt.plot(x_4000, total_lines_par_16_4000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_4000, total_lines_par_64_4000, color='black')
plt.plot(x_4000, total_lines_par_64_4000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_4000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_4000, it_seq_4000, color='gray')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_4000, it_par_2_4000, color='orange')
plt.plot(x_4000, it_par_2_4000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_4000, it_par_4_4000, color='red')
plt.plot(x_4000, it_par_4_4000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_4000, it_par_8_4000, color='purple')
plt.plot(x_4000, it_par_8_4000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_4000, it_par_16_4000, color='blue')
plt.plot(x_4000, it_par_16_4000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_4000, it_par_64_4000, color='black')
plt.plot(x_4000, it_par_64_4000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_4000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_4000, time_seq_4000, color='gray')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_4000, time_par_2_4000, color='orange')
plt.plot(x_4000, time_par_2_4000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_4000, time_par_8_4000, color='purple')
plt.plot(x_4000, time_par_8_4000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_4000, time_par_16_4000, color='blue')
plt.plot(x_4000, time_par_16_4000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_4000, time_par_64_4000, color='black')
plt.plot(x_4000, time_par_64_4000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_4000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_4000, speedup_2_4000, color='orange')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='orange', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_4000, speedup_4_4000, color='red')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='red', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_4000, speedup_8_4000, color='purple')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='purple', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_4000, speedup_16_4000, color='blue')
plt.plot(x_4000, speedup_16_4000, linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_4000, speedup_64_4000, color='black')
plt.plot(x_4000, speedup_64_4000, linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_N_speedup_4000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Total Number of Used Rows using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_10000, it_seq_10000, color='gray')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_10000, total_lines_par_2_10000, color='orange')
plt.plot(x_10000, total_lines_par_2_10000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_10000, total_lines_par_4_10000, color='red')
plt.plot(x_10000, total_lines_par_4_10000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_10000, total_lines_par_8_10000, color='purple')
plt.plot(x_10000, total_lines_par_8_10000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_10000, total_lines_par_16_10000, color='blue')
plt.plot(x_10000, total_lines_par_16_10000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_10000, total_lines_par_64_10000, color='black')
plt.plot(x_10000, total_lines_par_64_10000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_N_rows_10000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_10000, it_seq_10000, color='gray')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_10000, it_par_2_10000, color='orange')
plt.plot(x_10000, it_par_2_10000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_10000, it_par_4_10000, color='red')
plt.plot(x_10000, it_par_4_10000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_10000, it_par_8_10000, color='purple')
plt.plot(x_10000, it_par_8_10000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_10000, it_par_16_10000, color='blue')
plt.plot(x_10000, it_par_16_10000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_10000, it_par_64_10000, color='black')
plt.plot(x_10000, it_par_64_10000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_N_it_10000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_10000, time_seq_10000, color='gray')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='gray', label=r'RK', marker='s', markersize=10)
# plt.scatter(x_10000, time_par_2_10000, color='orange')
plt.plot(x_10000, time_par_2_10000, linewidth=1.5, color='orange', label=r'RKA with 2 Threads', marker='v', markersize=10)
# plt.scatter(x_10000, time_par_4_10000, color='red')
plt.plot(x_10000, time_par_4_10000, linewidth=1.5, color='red', label=r'RKA with 4 Threads', marker='o', markersize=10)
# plt.scatter(x_10000, time_par_8_10000, color='purple')
plt.plot(x_10000, time_par_8_10000, linewidth=1.5, color='purple', label=r'RKA with 8 Threads', marker='X', markersize=10)
# plt.scatter(x_10000, time_par_16_10000, color='blue')
plt.plot(x_10000, time_par_16_10000, linewidth=1.5, color='blue', label=r'RKA with 16 Threads', marker='^', markersize=10)
# plt.scatter(x_10000, time_par_64_10000, color='black')
plt.plot(x_10000, time_par_64_10000, linewidth=1.5, color='black', label=r'RKA with 64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_N_time_10000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_10000, speedup_2_10000, color='orange')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='orange', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_10000, speedup_4_10000, color='red')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='red', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_10000, speedup_8_10000, color='purple')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='purple', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_10000, speedup_16_10000, color='blue')
plt.plot(x_10000, speedup_16_10000, linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_10000, speedup_64_10000, color='black')
plt.plot(x_10000, speedup_64_10000, linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_N_speedup_10000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()