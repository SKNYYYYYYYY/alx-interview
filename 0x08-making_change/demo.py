def count_recur(coins, n, sum):
    if sum == 0:
        return 1
    if sum < 0 or n == 0:
        return 0
    return count_recur(coins, n, sum-coins[n-1]) + count_recur(coins, n-1, sum)

if __name__=='__main__':
    coins = [2, 5, 3, 6]
    sum = 37
    comb = count_recur(coins, len(coins), sum)
    print(comb)