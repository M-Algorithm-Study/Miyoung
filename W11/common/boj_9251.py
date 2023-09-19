# str1 = 'ACAYKP'
# str2 = 'CAPCAK'

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # 같으면 -1,-1  에 + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 다르면 왼쪽과 위쪽 중 max값

print(dp[-1][-1])

'''
     0 C A P C A K
  0  0 0 0 0 0 0 0
  A  0 0 1 1 1 1 1
  C  0 1 1 1 2 2 2
  A  0 1 2 2 2 3 3
  Y  0 1 2 2 2 3 3
  K  0 1 2 2 2 3 4
  P  0 1 2 3 3 3 4

'''