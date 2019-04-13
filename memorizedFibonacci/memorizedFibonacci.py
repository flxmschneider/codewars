cache = dict()

def fibonacci(n):
    if n in cache.keys():
        return cache[n]
    if n in [0, 1]:
        return n
    cache[n] = fibonacci(n-1) + fibonacci(n -2)
    return cache[n]
