# Matrix Multiplication using Multithreading (CPU)

## Objective

To analyze the performance of matrix multiplication using multiple threads and observe how execution time varies with increasing number of threads.

## Tools & Technologies

* Python
* NumPy (for matrix operations)
* Multiprocessing (for parallel execution)
* Matplotlib (for plotting graph)
* Psutil (for CPU usage monitoring)

## Methodology

1. A constant matrix of size **1200 × 1200** is generated.
2. For each iteration:

   * A random matrix of the same size is created.
   * Matrix multiplication is performed using NumPy.
3. Multiprocessing is used to run multiple matrix multiplications in parallel.
4. Number of threads is varied from **1 to 24**.
5. Execution time is recorded for each case.
6. A graph is plotted: **Threads vs Execution Time**.

## Result Table

| Threads | Time (minutes) |
| ------- | -------------- |
| 1       | 0.071          |
| 2       | 0.058          |
| 3       | 0.063          |
| 4       | 0.068          |
| 5       | 0.075          |
| 6       | 0.086          |
| 7       | 0.097          |
| 8       | 0.110          |
| 9       | 0.115          |
| 10      | 0.126          |
| 11      | 0.134          |
| 12      | 0.144          |
| 13      | 0.152          |
| 14      | 0.168          |
| 15      | 0.172          |
| 16      | 0.182          |
| 17      | 0.188          |
| 18      | 0.199          |
| 19      | 0.209          |
| 20      | 0.222          |
| 21      | 0.230          |
| 22      | 0.239          |
| 23      | 0.250          |
| 24      | 0.273          |

## 🖥 CPU Usage

CPU usage was monitored using `psutil`, showing how workload is distributed across cores.

## System Constraints

Due to hardware limitations (16 GB RAM), the experiment was conducted with:

* Matrix size: **1200 × 1200**
* Number of matrices: **50**

The implementation is scalable to larger sizes (e.g., 5000 × 5000).

## Observations

* Execution time initially decreases from 1 to 2 threads.
* After a certain point, execution time **increases** with more threads.

## Conclusion

Increasing the number of threads does not always improve performance. Beyond an optimal number of threads, execution time increases due to system overhead and resource contention.
