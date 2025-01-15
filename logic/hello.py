import numpy as np

def fibonacci(n, dp=None):
    if dp is None:
        dp = [-1] * (n + 1)
    
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)
    return dp[n]

msg = "Roll a dice!"
print(msg)

cache_hard = [[[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(2)]

print(cache_hard[0][0][0][0][0])


