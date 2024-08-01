import threading
import time
import numpy as np


def worker(array, start, end, result, index):
    result[index] = np.sum(array[start:end])

"""array — массив, в котором мы будем считать сумму.
start, end — индексы начала и конца части массива для текущего потока.
result — общий список, где каждый поток записывает свою сумму.
index — индекс в списке result, куда поток записывает свою сумму."""


if __name__ == '__main__':
    array = np.random.rand(10000000)
    num_threads = 4
    result = [0] * num_threads
    threads = []
    chunk_size = len(array) // num_threads

    start_time = time.time()

    """Создаем массив array из 10 миллионов случайных чисел.
Указываем количество потоков num_threads.
Создаем список result для хранения результатов работы каждого потока.
threads — список для хранения объектов потоков.
chunk_size — размер части массива для каждого потока."""

    # Цикл создает и запускает потоки

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(array)

        # Затем вызываем воркера
        thread = threading.Thread(target=worker, args=(array, start, end, result, i))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков.
    for thread in threads:
        thread.join()

    total_sum = np.sum(result)
    end_time = time.time()

    print(f"Многопоточный вариант. Итоговая сумма: {total_sum}")
    print(f"Многопоточный вариант: {end_time - start_time} секунд")
