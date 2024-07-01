import multiprocessing
import math

def is_prime(n):
    """Sprawdza, czy liczba n jest liczba pierwsza."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(start, end):
    """Znajduje pary blizniaczych liczb pierwszych w zakresie od start do end."""
    twin_primes = []
    previous_prime = None

    for num in range(start, end):
        if is_prime(num):
            if previous_prime is not None and num - previous_prime == 2:
                twin_primes.append((previous_prime, num))
            previous_prime = num

    return twin_primes

def worker(start, end, queue):
    """Funkcja pracownika do uruchomienia w osobnym procesie."""
    result = find_twin_primes(start, end)
    queue.put(result)

def main():
    range_start = 1
    range_end = 1000000
    num_processes = 8

    step = (range_end - range_start) // num_processes
    processes = []
    queue = multiprocessing.Queue()

    for i in range(num_processes):
        start = range_start + i * step
        end = start + step if i < num_processes - 1 else range_end
        process = multiprocessing.Process(target=worker, args=(start, end, queue))
        processes.append(process)
        process.start()

    twin_primes = []
    for _ in range(num_processes):
        twin_primes.extend(queue.get())

    for process in processes:
        process.join()

    print(twin_primes)

if __name__ == "__main__":
    main()
