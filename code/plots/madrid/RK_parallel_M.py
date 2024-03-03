import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/madrid/RK_parallel_M.py

filename = "outputs/omp/RK.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))

filename = "outputs/omp/RK_parallel.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_par = []
for i in range(file_size):
	time_par.append(float(lines[i].split()[2]))

time_par_1 = time_par[0::6]
time_par_2 = time_par[1::6]
time_par_4 = time_par[2::6]
time_par_8 = time_par[3::6]
time_par_16 = time_par[4::6]
time_par_64 = time_par[5::6]

time_seq_2000 = time_seq[0:5]
time_par_1_2000 = time_par_1[0:5]
time_par_2_2000 = time_par_2[0:5]
time_par_4_2000 = time_par_4[0:5]
time_par_8_2000 = time_par_8[0:5]
time_par_16_2000 = time_par_16[0:5]
time_par_64_2000 = time_par_64[0:5]
speedup_2_2000 = [time_par_1_2000[i]/time_par_2_2000[i] for i in range(5)]
speedup_4_2000 = [time_par_1_2000[i]/time_par_4_2000[i] for i in range(5)]
speedup_8_2000 = [time_par_1_2000[i]/time_par_8_2000[i] for i in range(5)]
speedup_16_2000 = [time_par_1_2000[i]/time_par_16_2000[i] for i in range(5)]
speedup_64_2000 = [time_par_1_2000[i]/time_par_64_2000[i] for i in range(5)]
x_2000 = [50, 100, 200, 500, 750]

time_seq_4000 = time_seq[5:11]
time_par_1_4000 = time_par_1[5:11]
time_par_2_4000 = time_par_2[5:11]
time_par_4_4000 = time_par_4[5:11]
time_par_8_4000 = time_par_8[5:11]
time_par_16_4000 = time_par_16[5:11]
time_par_64_4000 = time_par_64[5:11]
speedup_2_4000 = [time_par_1_4000[i]/time_par_2_4000[i] for i in range(6)]
speedup_4_4000 = [time_par_1_4000[i]/time_par_4_4000[i] for i in range(6)]
speedup_8_4000 = [time_par_1_4000[i]/time_par_8_4000[i] for i in range(6)]
speedup_16_4000 = [time_par_1_4000[i]/time_par_16_4000[i] for i in range(6)]
speedup_64_4000 = [time_par_1_4000[i]/time_par_64_4000[i] for i in range(6)]
x_4000 = [50, 100, 200, 500, 750, 1000]

time_seq_20000 = time_seq[11:19]
time_par_1_20000 = time_par_1[11:19]
time_par_2_20000 = time_par_2[11:19]
time_par_4_20000 = time_par_4[11:19]
time_par_8_20000 = time_par_8[11:19]
time_par_16_20000 = time_par_16[11:19]
time_par_64_20000 = time_par_64[11:19]
speedup_2_20000 = [time_par_1_20000[i]/time_par_2_20000[i] for i in range(8)]
speedup_4_20000 = [time_par_1_20000[i]/time_par_4_20000[i] for i in range(8)]
speedup_8_20000 = [time_par_1_20000[i]/time_par_8_20000[i] for i in range(8)]
speedup_16_20000 = [time_par_1_20000[i]/time_par_16_20000[i] for i in range(8)]
speedup_64_20000 = [time_par_1_20000[i]/time_par_64_20000[i] for i in range(8)]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]

time_seq_40000 = time_seq[19:28]
time_par_1_40000 = time_par_1[19:28]
time_par_2_40000 = time_par_2[19:28]
time_par_4_40000 = time_par_4[19:28]
time_par_8_40000 = time_par_8[19:28]
time_par_16_40000 = time_par_16[19:28]
time_par_64_40000 = time_par_64[19:28]
speedup_2_40000 = [time_par_1_40000[i]/time_par_2_40000[i] for i in range(9)]
speedup_4_40000 = [time_par_1_40000[i]/time_par_4_40000[i] for i in range(9)]
speedup_8_40000 = [time_par_1_40000[i]/time_par_8_40000[i] for i in range(9)]
speedup_16_40000 = [time_par_1_40000[i]/time_par_16_40000[i] for i in range(9)]
speedup_64_40000 = [time_par_1_40000[i]/time_par_64_40000[i] for i in range(9)]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

time_seq_80000 = time_seq[28:38]
time_par_1_80000 = time_par_1[28:38]
time_par_2_80000 = time_par_2[28:38]
time_par_4_80000 = time_par_4[28:38]
time_par_8_80000 = time_par_8[28:38]
time_par_16_80000 = time_par_16[28:38]
time_par_64_80000 = time_par_64[28:38]
speedup_2_80000 = [time_par_1_80000[i]/time_par_2_80000[i] for i in range(10)]
speedup_4_80000 = [time_par_1_80000[i]/time_par_4_80000[i] for i in range(10)]
speedup_8_80000 = [time_par_1_80000[i]/time_par_8_80000[i] for i in range(10)]
speedup_16_80000 = [time_par_1_80000[i]/time_par_16_80000[i] for i in range(10)]
speedup_64_80000 = [time_par_1_80000[i]/time_par_64_80000[i] for i in range(10)]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000, 20000]

time_seq_160000 = time_seq[38:48]
time_par_1_160000 = time_par_1[38:48]
time_par_2_160000 = time_par_2[38:48]
time_par_4_160000 = time_par_4[38:48]
time_par_8_160000 = time_par_8[38:48]
time_par_16_160000 = time_par_16[38:48]
time_par_64_160000 = time_par_64[38:48]
speedup_2_160000 = [time_par_1_160000[i]/time_par_2_160000[i] for i in range(10)]
speedup_4_160000 = [time_par_1_160000[i]/time_par_4_160000[i] for i in range(10)]
speedup_8_160000 = [time_par_1_160000[i]/time_par_8_160000[i] for i in range(10)]
speedup_16_160000 = [time_par_1_160000[i]/time_par_16_160000[i] for i in range(10)]
speedup_64_160000 = [time_par_1_160000[i]/time_par_64_160000[i] for i in range(10)]
x_160000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000, 20000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_1_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='purple', label=r'1 Thread - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_1_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_1_160000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 160000$', marker='^', markersize=10)
# plt.scatter(x_20000[2::], time_par_2_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_2_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_2_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_2_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_2_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_2_80000[2::], linestyle='--', linewidth=1.5, color='purple', label=r'2 Threads - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_2_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_2_160000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_2"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_1_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='purple', label=r'1 Thread - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_1_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_1_160000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 160000$', marker='^', markersize=10)
# plt.scatter(x_20000[2::], time_par_4_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_4_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_4_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_4_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_4_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_4_80000[2::], linestyle='--', linewidth=1.5, color='purple', label=r'4 Threads - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_4_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_4_160000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_4"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_1_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='purple', label=r'1 Thread - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_1_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_1_160000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 160000$', marker='^', markersize=10)
# plt.scatter(x_20000[2::], time_par_8_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_8_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_8_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_8_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_8_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_8_80000[2::], linestyle='--', linewidth=1.5, color='purple', label=r'8 Threads - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_8_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_8_160000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_8"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_1_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='purple', label=r'1 Thread - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_1_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_1_160000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 160000$', marker='^', markersize=10)
# plt.scatter(x_20000[2::], time_par_16_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_16_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'16 Threads - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_16_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_16_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'16 Threads - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_16_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_16_80000[2::], linestyle='--', linewidth=1.5, color='purple', label=r'16 Threads - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_16_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_16_160000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'16 Threads - $m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_16"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_1_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='purple', label=r'1 Thread - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_1_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_1_160000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 160000$', marker='^', markersize=10)
# plt.scatter(x_20000[2::], time_par_64_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_64_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'64 Threads - $m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_64_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_64_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'64 Threads - $m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_64_80000[2::], color='purple')
plt.plot(x_80000[2::], time_par_64_80000[2::], linestyle='--', linewidth=1.5, color='purple', label=r'64 Threads - $m = 80000$', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_64_160000[2::], color='blue')
plt.plot(x_160000[2::], time_par_64_160000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'64 Threads - $m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_64"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 2 threads"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], speedup_2_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_2_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], speedup_2_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_2_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], speedup_2_80000[2::], color='purple')
plt.plot(x_80000[2::], speedup_2_80000[2::], linewidth=1.5, color='purple', label=r'$m = 80000$', marker='X', markersize=10)
# plt.scatter(x_80000[2::], speedup_2_160000[2::], color='blue')
plt.plot(x_80000[2::], speedup_2_160000[2::], linewidth=1.5, color='blue', label=r'$m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_2"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 4 threads"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], speedup_4_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_4_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], speedup_4_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_4_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], speedup_4_80000[2::], color='purple')
plt.plot(x_80000[2::], speedup_4_80000[2::], linewidth=1.5, color='purple', label=r'$m = 80000$', marker='X', markersize=10)
# plt.scatter(x_80000[2::], speedup_4_160000[2::], color='blue')
plt.plot(x_80000[2::], speedup_4_160000[2::], linewidth=1.5, color='blue', label=r'$m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_4"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 8 threads"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], speedup_8_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_8_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], speedup_8_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_8_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], speedup_8_80000[2::], color='purple')
plt.plot(x_80000[2::], speedup_8_80000[2::], linewidth=1.5, color='purple', label=r'$m = 80000$', marker='X', markersize=10)
# plt.scatter(x_80000[2::], speedup_8_160000[2::], color='blue')
plt.plot(x_80000[2::], speedup_8_160000[2::], linewidth=1.5, color='blue', label=r'$m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_8"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 16 threads"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], speedup_16_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_16_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], speedup_16_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_16_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], speedup_16_80000[2::], color='purple')
plt.plot(x_80000[2::], speedup_16_80000[2::], linewidth=1.5, color='purple', label=r'$m = 80000$', marker='X', markersize=10)
# plt.scatter(x_80000[2::], speedup_16_160000[2::], color='blue')
plt.plot(x_80000[2::], speedup_16_160000[2::], linewidth=1.5, color='blue', label=r'$m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_16"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 64 threads"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], speedup_64_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_64_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$', marker='s', markersize=10)
# plt.scatter(x_40000[2::], speedup_64_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_64_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$', marker='o', markersize=10)
# plt.scatter(x_80000[2::], speedup_64_80000[2::], color='purple')
plt.plot(x_80000[2::], speedup_64_80000[2::], linewidth=1.5, color='purple', label=r'$m = 80000$', marker='X', markersize=10)
# plt.scatter(x_80000[2::], speedup_64_160000[2::], color='blue')
plt.plot(x_80000[2::], speedup_64_160000[2::], linewidth=1.5, color='blue', label=r'$m = 160000$', marker='^', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_64"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 20000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], speedup_2_20000[2::], linewidth=1.5, color='yellow')
plt.plot(x_20000[2::], speedup_2_20000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_20000[2::], speedup_4_20000[2::], linewidth=1.5, color='orange')
plt.plot(x_20000[2::], speedup_4_20000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_20000[2::], speedup_8_20000[2::], linewidth=1.5, color='red')
plt.plot(x_20000[2::], speedup_8_20000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_20000[2::], speedup_16_20000[2::], linewidth=1.5, color='blue')
plt.plot(x_20000[2::], speedup_16_20000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_20000[2::], speedup_64_20000[2::], linewidth=1.5, color='black')
plt.plot(x_20000[2::], speedup_64_20000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_20000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 40000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_40000[2::], speedup_2_40000[2::], linewidth=1.5, color='yellow')
plt.plot(x_40000[2::], speedup_2_40000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_40000[2::], speedup_4_40000[2::], linewidth=1.5, color='orange')
plt.plot(x_40000[2::], speedup_4_40000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_40000[2::], speedup_8_40000[2::], linewidth=1.5, color='red')
plt.plot(x_40000[2::], speedup_8_40000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_40000[2::], speedup_16_40000[2::], linewidth=1.5, color='blue')
plt.plot(x_40000[2::], speedup_16_40000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_40000[2::], speedup_64_40000[2::], linewidth=1.5, color='black')
plt.plot(x_40000[2::], speedup_64_40000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_40000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 80000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_80000[2::], speedup_2_80000[2::], linewidth=1.5, color='yellow')
plt.plot(x_80000[2::], speedup_2_80000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_80000[2::], speedup_4_80000[2::], linewidth=1.5, color='orange')
plt.plot(x_80000[2::], speedup_4_80000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_80000[2::], speedup_8_80000[2::], linewidth=1.5, color='red')
plt.plot(x_80000[2::], speedup_8_80000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_80000[2::], speedup_16_80000[2::], linewidth=1.5, color='blue')
plt.plot(x_80000[2::], speedup_16_80000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_80000[2::], speedup_64_80000[2::], linewidth=1.5, color='black')
plt.plot(x_80000[2::], speedup_64_80000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_80000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 160000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_160000[2::], speedup_2_160000[2::], linewidth=1.5, color='yellow')
plt.plot(x_160000[2::], speedup_2_160000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_160000[2::], speedup_4_160000[2::], linewidth=1.5, color='orange')
plt.plot(x_160000[2::], speedup_4_160000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_160000[2::], speedup_8_160000[2::], linewidth=1.5, color='red')
plt.plot(x_160000[2::], speedup_8_160000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_160000[2::], speedup_16_160000[2::], linewidth=1.5, color='blue')
plt.plot(x_160000[2::], speedup_16_160000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_160000[2::], speedup_64_160000[2::], linewidth=1.5, color='black')
plt.plot(x_160000[2::], speedup_64_160000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_M_speedup_160000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 20000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_20000[2::], time_par_2_20000[2::], linewidth=1.5, color='yellow')
plt.plot(x_20000[2::], time_par_2_20000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_20000[2::], time_par_4_20000[2::], linewidth=1.5, color='orange')
plt.plot(x_20000[2::], time_par_4_20000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_20000[2::], time_par_8_20000[2::], linewidth=1.5, color='red')
plt.plot(x_20000[2::], time_par_8_20000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_20000[2::], time_par_16_20000[2::], linewidth=1.5, color='blue')
plt.plot(x_20000[2::], time_par_16_20000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_20000[2::], time_par_64_20000[2::], linewidth=1.5, color='black')
plt.plot(x_20000[2::], time_par_64_20000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_20000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 40000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_40000[2::], time_par_2_40000[2::], linewidth=1.5, color='yellow')
plt.plot(x_40000[2::], time_par_2_40000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_40000[2::], time_par_4_40000[2::], linewidth=1.5, color='orange')
plt.plot(x_40000[2::], time_par_4_40000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_40000[2::], time_par_8_40000[2::], linewidth=1.5, color='red')
plt.plot(x_40000[2::], time_par_8_40000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_40000[2::], time_par_16_40000[2::], linewidth=1.5, color='blue')
plt.plot(x_40000[2::], time_par_16_40000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_40000[2::], time_par_64_40000[2::], linewidth=1.5, color='black')
plt.plot(x_40000[2::], time_par_64_40000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_40000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 80000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_80000[2::], time_par_2_80000[2::], linewidth=1.5, color='yellow')
plt.plot(x_80000[2::], time_par_2_80000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_80000[2::], time_par_4_80000[2::], linewidth=1.5, color='orange')
plt.plot(x_80000[2::], time_par_4_80000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_80000[2::], time_par_8_80000[2::], linewidth=1.5, color='red')
plt.plot(x_80000[2::], time_par_8_80000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_80000[2::], time_par_16_80000[2::], linewidth=1.5, color='blue')
plt.plot(x_80000[2::], time_par_16_80000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_80000[2::], time_par_64_80000[2::], linewidth=1.5, color='black')
plt.plot(x_80000[2::], time_par_64_80000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_80000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$m = 160000$"

fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_160000[2::], time_par_2_160000[2::], linewidth=1.5, color='yellow')
plt.plot(x_160000[2::], time_par_2_160000[2::], linewidth=1.5, color='yellow', label=r'2 Threads', marker='s', markersize=10)
# plt.scatter(x_160000[2::], time_par_4_160000[2::], linewidth=1.5, color='orange')
plt.plot(x_160000[2::], time_par_4_160000[2::], linewidth=1.5, color='orange', label=r'4 Threads', marker='o', markersize=10)
# plt.scatter(x_160000[2::], time_par_8_160000[2::], linewidth=1.5, color='red')
plt.plot(x_160000[2::], time_par_8_160000[2::], linewidth=1.5, color='red', label=r'8 Threads', marker='X', markersize=10)
# plt.scatter(x_160000[2::], time_par_16_160000[2::], linewidth=1.5, color='blue')
plt.plot(x_160000[2::], time_par_16_160000[2::], linewidth=1.5, color='blue', label=r'16 Threads', marker='^', markersize=10)
# plt.scatter(x_160000[2::], time_par_64_160000[2::], linewidth=1.5, color='black')
plt.plot(x_160000[2::], time_par_64_160000[2::], linewidth=1.5, color='black', label=r'64 Threads', marker='*', markersize=10)
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_M_time_160000"

# plt.show()
fig.savefig("plots/madrid/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/madrid/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()