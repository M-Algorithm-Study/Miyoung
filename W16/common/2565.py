# 저ㄴ깃줄의 개수
n = int(input()) 
lines = [] # 전깃줄 정보 리스트
for _ in range(n):
    a, b = map(int, input().split()) # A 전봇대와 B 전봇대에 연결된 위치 인풋
    lines.append((a, b)) # 리스트에 추가
lines.sort() # 

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
