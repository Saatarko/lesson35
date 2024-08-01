import time
import numpy as np


if __name__ == '__main__':
    array = np.random.rand(10000000)

    start_time = time.time()

    total_sum = np.sum(array)

    end_time = time.time()

    print(f"Последовательный вариант. Итоговая сумма: {total_sum}")
    print(f"Последовательный вариант.Заняло времени: {end_time - start_time} секунд")

