def fibonacci(n): 
    if n <= 1: return n

    prev2, prev1 = 0, 1

    for i in range(2, n + 1): 
        prev1, prev2 = prev1 + prev2, prev1

    return prev1

print(fibonacci(10))

