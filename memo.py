def fibonacci(n, cache={}):
    if n < 0: 
        raise ValueError("Should be a positive number")
    
    if n == 0: return 0 
    if n ==  1: return 1

    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

if __name__ == "__main__":
    print(fibonacci(10))  # Output: 55

