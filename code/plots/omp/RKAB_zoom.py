import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# python3 plots/omp/RKAB_zoom.py

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

time_par_1 = time[1::12]
time_par_2 = time[3::12]
time_par_4 = time[5::12]
time_par_8 = time[7::12]
time_par_16 = time[9::12]
time_par_64 = time[11::12]

it_par_1 = it[1::12]
it_par_2 = it[3::12]
it_par_4 = it[5::12]
it_par_8 = it[7::12]
it_par_16 = it[9::12]
it_par_64 = it[11::12]

blocks = [5, 10, 100, 500, 1000, 2000, 4000, 10000]

lines_par_2 = [it_par_2[i]*2*blocks[i%8] for i in range(len(it_par_2))]
lines_par_4 = [it_par_4[i]*4*blocks[i%8] for i in range(len(it_par_4))]
lines_par_8 = [it_par_8[i]*8*blocks[i%8] for i in range(len(it_par_8))]
lines_par_16 = [it_par_16[i]*16*blocks[i%8] for i in range(len(it_par_16))]
lines_par_64 = [it_par_64[i]*64*blocks[i%8] for i in range(len(it_par_64))]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = [5, 10, 100, 500, 1000, 2000, 4000, 10000]

plot_title = r"$4000 \times 1000$"

fig, ax = plt.subplots(figsize=(10, 7))

ax.axhline(y=it_seq_dim[0], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
ax.scatter(x, it_par_2[0:8], color='orange')
ax.plot(x, it_par_2[0:8], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
ax.scatter(x, it_par_4[0:8], color='red')
ax.plot(x, it_par_4[0:8], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
ax.scatter(x, it_par_8[0:8], color='purple')
ax.plot(x, it_par_8[0:8], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
ax.scatter(x, it_par_16[0:8], color='blue')
ax.plot(x, it_par_16[0:8], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
ax.scatter(x, it_par_64[0:8], color='black')
ax.plot(x, it_par_64[0:8], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)

ax.grid()
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

axins = zoomed_inset_axes(ax, 25, loc=1)

axins.axhline(y=it_seq_dim[0], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
axins.scatter(x, it_par_2[0:8], color='orange')
axins.plot(x, it_par_2[0:8], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
axins.scatter(x, it_par_4[0:8], color='red')
axins.plot(x, it_par_4[0:8], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
axins.scatter(x, it_par_8[0:8], color='purple')
axins.plot(x, it_par_8[0:8], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
axins.scatter(x, it_par_16[0:8], color='blue')
axins.plot(x, it_par_16[0:8], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
axins.scatter(x, it_par_64[0:8], color='black')
axins.plot(x, it_par_64[0:8], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
axins.set_xlim(x[3]-30, x[3]+30)
axins.set_ylim(it_par_2[3]-15, it_par_2[3]+15)

plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

ax.legend(loc=2)

filename_fig = "RKAB_zoom_it_4000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 1000$"

fig, ax = plt.subplots(figsize=(10, 7))

ax.axhline(y=it_seq_dim[6], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
ax.scatter(x, it_par_2[48:56], color='orange')
ax.plot(x, it_par_2[48:56], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
ax.scatter(x, it_par_4[48:56], color='red')
ax.plot(x, it_par_4[48:56], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
ax.scatter(x, it_par_8[48:56], color='purple')
ax.plot(x, it_par_8[48:56], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
ax.scatter(x, it_par_16[48:56], color='blue')
ax.plot(x, it_par_16[48:56], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
ax.scatter(x, it_par_64[48:56], color='black')
ax.plot(x, it_par_64[48:56], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)

ax.grid()
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

axins = zoomed_inset_axes(ax, 10, loc=1)

axins.axhline(y=it_seq_dim[6], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
axins.scatter(x, it_par_2[48:56], color='orange')
axins.plot(x, it_par_2[48:56], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
axins.scatter(x, it_par_4[48:56], color='red')
axins.plot(x, it_par_4[48:56], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
axins.scatter(x, it_par_8[48:56], color='purple')
axins.plot(x, it_par_8[48:56], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
axins.scatter(x, it_par_16[48:56], color='blue')
axins.plot(x, it_par_16[48:56], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
axins.scatter(x, it_par_64[48:56], color='black')
axins.plot(x, it_par_64[48:56], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
axins.set_xlim(x[3]-30, x[3]+30)
axins.set_ylim(it_par_2[51]-15, it_par_2[51]+15)

plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

ax.legend(loc=2)

filename_fig = "RKAB_zoom_it_80000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

# plot_title = r"$20000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[1], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[8:16], color='orange')
# plt.plot(x, it_par_2[8:16], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[8:16], color='red')
# plt.plot(x, it_par_4[8:16], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[8:16], color='purple')
# plt.plot(x, it_par_8[8:16], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[8:16], color='blue')
# plt.plot(x, it_par_16[8:16], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[8:16], color='black')
# plt.plot(x, it_par_64[8:16], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_20000_1000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$20000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[2], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[16:24], color='orange')
# plt.plot(x, it_par_2[16:24], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[16:24], color='red')
# plt.plot(x, it_par_4[16:24], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[16:24], color='purple')
# plt.plot(x, it_par_8[16:24], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[16:24], color='blue')
# plt.plot(x, it_par_16[16:24], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[16:24], color='black')
# plt.plot(x, it_par_64[16:24], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_20000_4000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$40000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[3], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[24:32], color='orange')
# plt.plot(x, it_par_2[24:32], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[24:32], color='red')
# plt.plot(x, it_par_4[24:32], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[24:32], color='purple')
# plt.plot(x, it_par_8[24:32], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[24:32], color='blue')
# plt.plot(x, it_par_16[24:32], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[24:32], color='black')
# plt.plot(x, it_par_64[24:32], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_40000_1000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$40000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[4], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[32:40], color='orange')
# plt.plot(x, it_par_2[32:40], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[32:40], color='red')
# plt.plot(x, it_par_4[32:40], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[32:40], color='purple')
# plt.plot(x, it_par_8[32:40], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[32:40], color='blue')
# plt.plot(x, it_par_16[32:40], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[32:40], color='black')
# plt.plot(x, it_par_64[32:40], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_40000_4000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$40000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[5], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[40:48], color='orange')
# plt.plot(x, it_par_2[40:48], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[40:48], color='red')
# plt.plot(x, it_par_4[40:48], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[40:48], color='purple')
# plt.plot(x, it_par_8[40:48], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[40:48], color='blue')
# plt.plot(x, it_par_16[40:48], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[40:48], color='black')
# plt.plot(x, it_par_64[40:48], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_40000_10000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$80000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[6], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[48:56], color='orange')
# plt.plot(x, it_par_2[48:56], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[48:56], color='red')
# plt.plot(x, it_par_4[48:56], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[48:56], color='purple')
# plt.plot(x, it_par_8[48:56], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[48:56], color='blue')
# plt.plot(x, it_par_16[48:56], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[48:56], color='black')
# plt.plot(x, it_par_64[48:56], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_80000_1000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$80000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[7], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[56:64], color='orange')
# plt.plot(x, it_par_2[56:64], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[56:64], color='red')
# plt.plot(x, it_par_4[56:64], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[56:64], color='purple')
# plt.plot(x, it_par_8[56:64], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[56:64], color='blue')
# plt.plot(x, it_par_16[56:64], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[56:64], color='black')
# plt.plot(x, it_par_64[56:64], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_80000_4000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$80000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[8], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[64:72], color='orange')
# plt.plot(x, it_par_2[64:72], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[64:72], color='red')
# plt.plot(x, it_par_4[64:72], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[64:72], color='purple')
# plt.plot(x, it_par_8[64:72], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[64:72], color='blue')
# plt.plot(x, it_par_16[64:72], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[64:72], color='black')
# plt.plot(x, it_par_64[64:72], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_80000_10000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$160000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[9], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[72:80], color='orange')
# plt.plot(x, it_par_2[72:80], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[72:80], color='red')
# plt.plot(x, it_par_4[72:80], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[72:80], color='purple')
# plt.plot(x, it_par_8[72:80], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[72:80], color='blue')
# plt.plot(x, it_par_16[72:80], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[72:80], color='black')
# plt.plot(x, it_par_64[72:80], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_160000_1000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$160000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[10], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[80:88], color='orange')
# plt.plot(x, it_par_2[80:88], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[80:88], color='red')
# plt.plot(x, it_par_4[80:88], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[80:88], color='purple')
# plt.plot(x, it_par_8[80:88], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[80:88], color='blue')
# plt.plot(x, it_par_16[80:88], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[80:88], color='black')
# plt.plot(x, it_par_64[80:88], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_160000_4000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()

# plot_title = r"$160000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[11], linestyle='--', linewidth=1.5, color='gray', label=r'Sequential')
# # plt.scatter(x, it_par_2[88:96], color='orange')
# plt.plot(x, it_par_2[88:96], linewidth=1.5, color='orange', label=r'Threads = 2', marker='s', markersize=10)
# # plt.scatter(x, it_par_4[88:96], color='red')
# plt.plot(x, it_par_4[88:96], linewidth=1.5, color='red', label=r'Threads = 4', marker='^', markersize=10)
# # plt.scatter(x, it_par_8[88:96], color='purple')
# plt.plot(x, it_par_8[88:96], linewidth=1.5, color='purple', label=r'Threads = 8', marker='X', markersize=10)
# # plt.scatter(x, it_par_16[88:96], color='blue')
# plt.plot(x, it_par_16[88:96], linewidth=1.5, color='blue', label=r'Threads = 16', marker='^', markersize=10)
# # plt.scatter(x, it_par_64[88:96], color='black')
# plt.plot(x, it_par_64[88:96], linewidth=1.5, color='black', label=r'Threads = 64', marker='v', markersize=10)
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Iterations')

# filename_fig = "RKAB_zoom_it_160000_10000"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
# plt.close()