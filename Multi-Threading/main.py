import numpy as np
import time
import multiprocessing
import matplotlib.pyplot as plt
import psutil


# Global variables for workers
CONSTANT_MATRIX = None
MATRIX_SIZE = None


# Initialize worker (runs once per process)
def init_worker(matrix_size, constant_matrix):
    global MATRIX_SIZE, CONSTANT_MATRIX
    MATRIX_SIZE = matrix_size
    CONSTANT_MATRIX = constant_matrix


# Worker function
def multiply_matrix(_):
    A = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    return np.dot(A, CONSTANT_MATRIX)


def run_experiment(matrix_size, num_matrices, num_threads, constant_matrix):
    print(f"\nRunning with {num_threads} threads...")

    start_time = time.time()

    with multiprocessing.Pool(
        processes=num_threads,
        initializer=init_worker,
        initargs=(matrix_size, constant_matrix)
    ) as pool:
        pool.map(multiply_matrix, range(num_matrices))

    end_time = time.time()

    total_time = (end_time - start_time) / 60
    print(f"Time Taken: {total_time:.2f} minutes")

    return total_time


def main():
    matrix_size = 1200
    num_matrices = 50

    constant_matrix = np.random.rand(matrix_size, matrix_size)

    max_threads = multiprocessing.cpu_count()

    print(f"Number of CPU cores: {max_threads}")

    times = []

    # 🔥 IMPORTANT: Limit threads to avoid crash
    thread_list = list(range(1, max_threads + 5))   # not 2x anymore

    for t in thread_list:
        try:
            time_taken = run_experiment(matrix_size, num_matrices, t, constant_matrix)
            times.append(time_taken)
        except Exception as e:
            print(f"Stopped at {t} threads due to system limits.")
            break

    # 📊 Print Table
    print("\nRESULT TABLE:")
    print("Threads:", thread_list[:len(times)])
    print("Time (min):", [round(x, 3) for x in times])

    # 📈 Graph
    plt.plot(thread_list[:len(times)], times, marker='o')
    plt.title("Execution Time vs Threads")
    plt.xlabel("Threads")
    plt.ylabel("Time (minutes)")
    plt.grid()
    plt.savefig("execution_time.png")
    plt.show()

    print("\nCPU Usage per core:")
    print(psutil.cpu_percent(percpu=True))


if __name__ == "__main__":
    main()