import sys
from collections import deque

dx = [-1, 0, 1, 0] # 좌우
dy = [0, 1, 0, -1] # 상하

def sink_BFS(x, y, h): # h는 물높이
    queue = deque() # 큐를 deque 자료 구조로 초기화
    queue.append((x, y)) # 시작점을 큐에 추가
    sink_table[x][y] = True  # .... 으 ... true 

    while queue: 
        x, y = queue.popleft()
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:
                sink_table[nx][ny] = True
                queue.append((nx, ny))

N = int(sys.stdin.readline()) # 지역의 크기
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 각 지점의 높이 정보를 저장
ans = 1

for k in range(max(map(max, water_board))): # 워터보드의 최대 높이 만큼 반복
    sink_table = [[False] * N for _ in range(N)] # 물에 잠긴 지역 초기화
    count = 0 # 안전영역 개수 초기화
    for i in range(N):     # 
        for j in range(N): # N * N 모든 지점을 확인
            if water_board[i][j] > k and not sink_table[i][j]: 
                # 현재 높이가 k보다 크고
                # 아직 물에 잠기지 않았다면
                count += 1 # 시작점에서 안전영역의 갯수 +1
                sink_BFS(i, j, k) # BFS 수행
    ans = max(ans, count)

print(ans)

# BFS는 아직 잘 모르겠다 ㅠㅠ , 잠기는 물높이도 아주 헷갈린다.