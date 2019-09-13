#!/usr/bin/env python3

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    secs = [5, 4, 3, 2, 1]
    # .map return an iterator that applies function to every item of iterable,
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
