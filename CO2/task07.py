Python
Run
import time
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Redesigned memoization method
memo = {}
memo_calls = 0

def ways_memo(n):
    global memo_calls

    if n in memo:
        return memo[n]

    memo_calls += 1

    if n <= 1:
        memo[n] = 1
    else:
        memo[n] = ways_memo(n - 1) + ways_memo(n - 2)

    return memo[n]


# Redesigned iterative method
def ways_loop(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# Compare all methods
print("COMPARISON OF THREE METHODS")

for n in [10, 20, 25, 30]:

    naive_calls = 0
    start = time.perf_counter()
    original = ways_naive(n)
    naive_time = time.perf_counter() - start

    memo.clear()
    memo_calls = 0
    start = time.perf_counter()
    improved = ways_memo(n)
    memo_time = time.perf_counter() - start

    start = time.perf_counter()
    iterative = ways_loop(n)
    loop_time = time.perf_counter() - start

    print("\nSteps:", n)
    print("Original result:", original)
    print("Original calls:", naive_calls)
    print("Original time:", round(naive_time, 6), "seconds")

    print("Memo result:", improved)
    print("Memo calls:", memo_calls)
    print("Memo time:", round(memo_time, 6), "seconds")

