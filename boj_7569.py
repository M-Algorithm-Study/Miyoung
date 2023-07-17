from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M) and (box[nx][ny][nz] == 0):
                queue.append([nx, ny, nz])
                box[nx][ny][nz] = box[x][y][z] + 1

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

max_day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            max_day = max(max_day, box[i][j][k])

print(max_day - 1)