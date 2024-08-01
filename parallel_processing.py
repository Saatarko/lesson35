import multiprocessing
import time
import numpy as np


def worker(array, start, end, result, index):
    result[index] = np.sum(array[start:end])

    """array — массив, в котором мы будем считать сумму.
    start, end — индексы начала и конца части массива для текущего потока.
    result — общий список, где каждый процесс записывает свою сумму.
    index — индекс в списке result, куда процесс записывает свою сумму."""


if __name__ == '__main__':
    array = np.random.rand(10000000)
    num_processes = 4
    result = multiprocessing.Array('d', num_processes)
    processes = []
    chunk_size = len(array) // num_processes

    start_time = time.time()

    # Цикл создает и запускает процессы

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

    print(f"Мультипроцессовый вариант. Итоговая сумма: {total_sum}")
    print(f"Мультипроцессовый вариант занял времени: {end_time - start_time} секунд")
