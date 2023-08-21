from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    board[0][0] = -1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] <= 0:
                board[nx][ny] = -1
                visited[nx][ny] = True
                q.append((nx, ny))

def melt():
    melting = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if board[ni][nj] == -1:
                        cnt += 1
                if cnt >= 2:
                    melting.append((i, j))
    for x, y in melting:
        board[x][y] = -1
    return len(melting) > 0

time = 0
while True:
    bfs()
    if not melt():
        break
    time += 1

print(time)
