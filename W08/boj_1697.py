from collections import deque

def bfs(n, k):     # n: 수빈(5), k: 동생(17)
    MAX = 100001   # 범위의 최대값 + 1 (0부터 시작하기 때문)
    v = [0] * MAX  # 각 위치에 도달하는데 걸린 시간을 저장하는 리스트
    q = deque([n]) # 초기값 : 수빈이의 위치 q = [5]

    while q: 
        c = q.popleft() # 최단 시간을 현재 시간으로 저장
        
        if c == k:  # 동생을 찾았다면
            return v[c] # 그 위치에 도달하는데 걸린 시간을 출력
        
        # c - 1 이 범위 내에 있고, 방문하지 않은경우
        if 0 <= c - 1 < MAX and not v[c - 1]:
            v[c - 1] = v[c] + 1 # -1 경로에 걸린 시간 기록& 방문표시
            q.append(c - 1) # 시간 -1
        
        # c + 1 이 범위 내에 있고, 방문하지 않은경우
        if 0 <= c + 1 < MAX and not v[c + 1]:
            v[c + 1] = v[c] + 1  # +1 경로에 걸린 시간 기록& 방문표시
            q.append(c + 1)  # 시간 +1
        
        # c * 2 가 범위 내에 있고, 방문하지 않은경우
        if 0 <= c * 2 < MAX and not v[c * 2]: 
            v[c * 2] = v[c] + 1 # *2 경로에 걸린 시간 기록& 방문표시
            q.append(c * 2) # 시간 *2
            
    return -1 # 동생을 찾지 못한경우 예외처리.

n, k = map(int, input().split())
print(bfs(n, k))
