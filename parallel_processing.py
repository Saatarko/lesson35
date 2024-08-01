import multiprocessing
import time
import numpy as np


def worker(array, start, end, result, index):
    result[index] = np.sum(array[start:end])


if __name__ == '__main__':
    array = np.random.rand(10000000)
    num_processes = 4
    result = multiprocessing.Array('d', num_processes)
    processes = []
    chunk_size = len(array) // num_processes

    start_time = time.time()

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_processes - 1 else len(array)
        process = multiprocessing.Process(target=worker, args=(array, start, end, result, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = sum(result)
    end_time = time.time()

    print(f"Total sum: {total_sum}")
    print(f"Time taken: {end_time - start_time} seconds")
