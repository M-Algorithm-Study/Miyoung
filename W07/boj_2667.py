n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    graph[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for r in sorted(result):
    print(r)