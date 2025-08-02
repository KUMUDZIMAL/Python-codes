def fibonacci(f0, f1, n):
    if n <= 0:
        return
    print(f0)
    fibonacci(f1, f0 + f1, n - 1)


f0 = 0
f1 = 1

num_terms = 10

fibonacci(f0, f1, num_terms)
