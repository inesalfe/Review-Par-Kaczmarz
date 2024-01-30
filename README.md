# Parallelization Strategies for the Randomized Kaczmarz Algorithm on Large-Scale Dense Systems

This repository containts the source code for testing approaches to the parallelization of the Kaczmarz method.

The paper describing the obtained results was submitted to the Journal of Parallel and Distributed Computing and its preprint is available in ArXiv.

# Requirements

* C++11
* OpenMp
* MPI
* Eigen Library (version 3.4)

### Python Packages (for plots)

* numpy
* matplotlib
* sys
* scipy

# Usage

Important note: Run all commands inside the code directory.

Compile all files:

```
make
```

Generate Consistent Data Sets:

```
./bin/genConsistDataSets.exe
```

Generate Inconsistent Data Sets:

```
./bin/genLSDataSets.exe
```

Run Parallel Kaczmarz (example with parallelization inside iterations):

Run the following command to compute the number of iterations:

```
./bin/RK_parallel_error.exe <data_set> <n_runs> <eps> <M> <N>
```

Run the following command to measure execution time for a given number of iterations:

```
./bin/RK_parallel_max_it.exe <data_set> <n_runs> <M> <N> <max_it_stop>
```

### Parameter options for the algorithms

__<data_set>__

All data sets are dense and entries are always generated from a normal distribution.

Options  | Average | Standard Deviation
------------- | ------------- | -------------
dense  | -5 to 5 | 1 to 20
dense_ls  | -5 to 5 | 1 to 20

For "dense_ls" gaussian noise was added to the right hand side of the every equation in the system.

__<n_runs>__

Value used for simulations: 10.

__<eps>__

Value used for simulations: $10^{-8}$.

__\<M\> and \<N\>__

M value Options: 2000, 4000, 20000, 40000, 80000, 160000. <br />
N value Options: 50, 100, 200, 500, 750, 1000, 2000, 4000, 10000, 20000.

Overdetermined systems were created such that M/N > 2.
