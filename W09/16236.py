from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 먹을 수 있는 물고기의 위치와 거리를 탐색
def bfs(x, y, size):
    v = [[0] * n for _ in range(n)]
    v[x][y] = 1
    queue = deque([(x, y)])
    fishes = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                # 자신의 크기보다 큰 물고기의 칸은 지나갈 수 없다
                if matrix[nx][ny] <= size or matrix[nx][ny] == 0:
                    v[nx][ny] = v[x][y] + 1
                    queue.append((nx, ny))
                # 자신의 크기보다 작은 물고기만 먹을 수 있다
                if 0 < matrix[nx][ny] < size:
                    fishes.append((nx, ny, v[nx][ny] - 1))
    return fishes

n = int(input())
matrix = []
shark_size, shark_eat, shark_x, shark_y = 2, 0, 0, 0

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(n):
        if row[j] == 9:
            shark_x, shark_y = i, j
            matrix[i][j] = 0

time = 0
while True:
    fishes = bfs(shark_x, shark_y, shark_size)
    if not fishes:  # 먹을 수 있는 물고기가 없다면 종료
        break
    fishes.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, x좌표, y좌표 순으로 정렬
    fish_x, fish_y, fish_distance = fishes[0]
    time += fish_distance
    matrix[fish_x][fish_y] = 0
    shark_eat += 1
    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0
    shark_x, shark_y = fish_x, fish_y

print(time)
