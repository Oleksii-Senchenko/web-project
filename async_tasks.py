import threading
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


res = is_prime(2)
print(res)


def timing_decorator(label):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{label} took {end - start:.4f} seconds.")
            return result
        return wrapper
    return decorator




# --------------------------------------------
@timing_decorator("Single-threaded")
def find_primes_single_thread(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


print(find_primes_single_thread(10, 30))


def find_primes_in_range(start, end, result):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)


@timing_decorator("Multi-threaded")
def find_primes_multi_thread(start, end):
    mid = (start + end) // 2

    part1 = []
    part2 = []

    thread1 = threading.Thread(target=find_primes_in_range, args=(start, mid, part1))
    thread2 = threading.Thread(target=find_primes_in_range, args=(mid + 1, end, part2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    result = part1 + part2

    return result

print(find_primes_multi_thread(10, 30))


def test_prime_functions():
    test_cases = [
        (10, 50),
        (1, 100),
        (100, 200),
        (200, 300),
        (50, 60),
    ]

    for start, end in test_cases:

        result_single = find_primes_single_thread(start, end)

        result_multi = find_primes_multi_thread(start, end)

        assert result_single == result_multi, f"Test failed for range {start}-{end}: Single: {result_single}, Multi: {result_multi}\n\n"

        print(f"\n\nTest passed for range {start}-{end}: {result_multi}")


test_prime_functions()



# The hour of the single-thread is used for 0 to 0.0002 seconds....
# The time of the multi-threading  (find_primes_multi_thread) varies from 0.0002 to 0.0004 seconds....
