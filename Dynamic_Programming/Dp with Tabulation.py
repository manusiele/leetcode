def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# definition : solves a problem by building up the solution from the bottom, starting with the base cases

# pseudocode

# F = array of length (n + 1)
# F[0] = 0
# F[1] = 1
# for i from 2 to n:
#     F[i] = F[i - 1] + F[i - 2]