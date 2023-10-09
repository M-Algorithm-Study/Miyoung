N = int(input())  # 수열의 길이
array = list(map(int, input().split())) # 수열

dp = [1] * N # 1로 초기화

for i in range(1, N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
