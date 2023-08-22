from collections import deque

n, m = map(int, input().split()) # 모눈종이 크기
board = [list(map(int, input().split())) for _ in range(n)] # 치즈 위치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(): # 외부의 공기와 접촉하는 치즈 부분을 찾는 함수 
    q = deque([(0, 0)]) # 시작점
    v = [[False] * m for _ in range(n)] # 방문 2차원 리스트
    v[0][0] = True # 시작점은 방문 체크
    board[0][0] = -1 # 가장자리는 공기 접촉되는 부분이므로 -1
    
    while q: 
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] # 상하좌우
            # ny, nx가 범위 내에 있고, 방문하지 않았으며 그 위치 값이 0이거나 -1(공기접촉)
            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and board[nx][ny] <= 0:
                board[nx][ny] = -1 # 공지 접촉 표시
                v[nx][ny] = True   # 방문 체크
                q.append((nx, ny))

def melt(): # 외부 공기와 2면 이상 접촉하는 치즈를 찾아 녹이는 함수
    melting = []
    for i in range(n):     # 모든 방향을 순회하며 치즈 찾기
        for j in range(m): 
            if board[i][j] == 1: # 현재 위치가 치즈라면
                cnt = 0
                for d in range(4): # 네 방향 중  몇 면이 외부공기와 접촉하는지 체크
                    ni, nj = i + dx[d], j + dy[d]
                    if board[ni][nj] == -1: # 공기와 접촉했다면 count
                        cnt += 1
                if cnt >= 2:
                    melting.append((i, j))
    for x, y in melting:
        board[x][y] = -1
    return len(melting) > 0 # 0보다 크면 True(melt 계속 진행), 0이면 False값을 받환해서 while문이 종료됨.

time = 0 # 치즈가 모두 녹는 데 걸리는 시간
while True:
    bfs() # 외부 공기와 접촉하는 치즈를 찾아서
    if not melt(): # 치즈가 더 이상 녹지 않으면 반복을 종료
        break
    time += 1

print(time)
