n = int(input())
dp = [0, 1] + [0] * (n-1) #초기값 0 1 

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1] # 이전값끼리 더하기 

print(dp[n])
