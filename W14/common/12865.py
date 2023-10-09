'''
평범한 배낭
'''
N, K = map(int, input().split()) # N 물품의 수, K 무게

items = []
for _ in range(N):
    W, V = map(int, input().split()) # W 물건 무게, K 물건 가치
    items.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)] # 가치를 저장할 2차원 리스트 초기화

for i in range(1, N + 1): # 물품수 기준
    for j in range(1, K + 1): # 무게 기준
        weight, value = items[i-1] # 현재 무게, 현재 가치

        if j < weight: # 현재 무게가 j 보다 클 경우
            dp[i][j] = dp[i-1][j] # 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])
