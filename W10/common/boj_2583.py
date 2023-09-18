from collections import deque

M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K): # 직사각형
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            paper[i][j] = 1 # 직사각형 구역을 1로 표시

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    paper[x][y] = 1  # 시작점 방문표시
    count = 1  # 영역크기 증가

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 영역 내이고, 방문 안한경우
            if 0 <= nx < M and 0 <= ny < N and paper[nx][ny] == 0:
                queue.append((nx, ny)) # 큐에 추가
                paper[nx][ny] = 1 # 방문 표시
                count += 1 # 영역크기 증가

    return count

areas = [] # 영역저장

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            areas.append(bfs(i, j)) 
            # return count가 되면서 areas리스트에 count가 하나씩 추가된다.

print(len(areas))
areas.sort()
print(" ".join(map(str, areas)))
