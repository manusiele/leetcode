# coins can have maximum values (like a limit on each coin’s value or maybe limited denominations)

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = list(map(int, input("Enter coin values separated by space: ").split()))
amount = int(input("Enter the amount: "))
print(coinChange(coins, amount))