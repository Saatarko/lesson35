import threading
import time
import numpy as np


def worker(array, start, end, result, index):
    result[index] = np.sum(array[start:end])


if __name__ == '__main__':
    array = np.random.rand(10000000)
    num_threads = 4
    result = [0] * num_threads
    threads = []
    chunk_size = len(array) // num_threads

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(array)
        thread = threading.Thread(target=worker, args=(array, start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = np.sum(result)
    end_time = time.time()

    print(f"Total sum: {total_sum}")
    print(f"Time taken: {end_time - start_time} seconds")
