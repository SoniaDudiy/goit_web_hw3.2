import multiprocessing
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    numbers = [128, 255, 99999, 10651060]

    # Синхронна версія
    start_time = time.time()
    for number in numbers:
        factorize(number)
    end_time = time.time()
    print(f"Синхронна версія виконана за {end_time - start_time} секунд")

    # Покращена версія
    start_time = time.time()
    pool = multiprocessing.Pool()
    pool.map(factorize, numbers)
    pool.close()
    pool.join()
    end_time = time.time()
    print(f"Покращена версія виконана за {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
