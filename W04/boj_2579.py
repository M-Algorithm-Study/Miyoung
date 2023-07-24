# 계단오르기
n = int(input()) # 6
stairs = [0] * n # 계단 리스트 생성
for i in range(n):
    stairs[i] = int(input())

dp = [0] * n # 각 계단까지의 도달 점수
dp[0] = stairs[0] # 첫번째 계단 도달 점수 = 첫번째계단
if n > 1: dp[1] = stairs[0] + stairs[1] # 계단 두개 : 두번째 계단 도달 점수 = 첫번째계단 + 두번째 계단
if n > 2: dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2]) # 계단 세개 : 세번째 계단 도달 점수 = max(두번째 계단 + 세번째계단 ,첫번째 계단 + 세번째 계단) 

for i in range(3, n): # 네번째 계단부터 마지막 계단까지 : n이 3 이하이면 수행하지않는다.
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
               # 첫번째 10 + 세번째계단 15 + 네번째 25 , 두번째 20 + 네번째 25  중에 큰 점수
print(dp[n-1]) # 인덱스는 0부터 이므로 n-1이 마지막 계단(인덱스)이다.


# 6
# 10 20 15 25 10 20
