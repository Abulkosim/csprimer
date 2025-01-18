def fib(n):
    back2, back1 = 0, 1
    if n == 0:
        return 0
    for _ in range(2, n):
        back1, back2 = back1 + back2, back1

    return back1 + back2


print(fib(5)) # 5
print(fib(10)) # 55
# 0, 1, 1, 2, 3, 5
