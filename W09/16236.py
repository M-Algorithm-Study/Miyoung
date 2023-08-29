from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 먹을 수 있는 물고기의 위치와 거리를 탐색
def bfs(x, y, size): # 아기상어 좌표, 사이즈
    v = [[0] * n for _ in range(n)] # 방문
    v[x][y] = 1  # 시작점 방문처리
    queue = deque([(x, y)]) # 시작점 추가
    fishes = [] # [(거리, x, y)...] 아기상어와의 거리와 물고기 위치를 저장
    while queue:
        x, y = queue.popleft() # 큐에서 위치를 pop
        for i in range(4): # 상하좌우 확인
            nx, ny = x + dx[i], y + dy[i] 
            # 공간안에 있고, 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]: 
                # 물고기가 아기상어보다 작거나 같고, 물고기가 없으면
                if matrix[nx][ny] <= size or matrix[nx][ny] == 0:
                    v[nx][ny] = v[x][y] + 1 # 거리 +1 (0이 아니면 방문)
                    queue.append((nx, ny)) # 위지정보 업데이트 
                # 자신의 크기보다 작은 물고기는 먹고 같으면 지나간다.
                if 0 < matrix[nx][ny] < size: # 크기가 작으면 
                    fishes.append((nx, ny, v[nx][ny] - 1)) # 
    return fishes



n = int(input()) # 공간의 크기
matrix = []  # 공간의 상태(물고기사이즈)
shark_size, shark_eat, shark_x, shark_y = 2, 0, 0, 0 # 아기상어크기, 먹은 물고기수, 아기상어 위치

for i in range(n): 
    row = list(map(int, input().split())) # 행에대한 정보를 입력 받아서
    matrix.append(row) # 2차원 리스트에 추가
    for j in range(n): # 행의 칸을 확인
        if row[j] == 9: # 아기상어 위치 확인
            shark_x, shark_y = i, j # 위치 추가
            matrix[i][j] = 0 # 아기상어 자리는 빈칸으로

time = 0 # 소요시간
while True: # 먹을 물고기가 없을때까지 반복
    fishes = bfs(shark_x, shark_y, shark_size)
    if not fishes:  # 먹을 수 있는 물고기가 없다면 종료
        break
    fishes.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, x좌표, y좌표 순으로 정렬
    fish_x, fish_y, fish_distance = fishes[0] # 가장 가까운 물고기 정보를 넣는다.
    time += fish_distance # 시간 업데이트
    matrix[fish_x][fish_y] = 0 # 물고기를 먹고 빈칸으로
    shark_eat += 1 # 먹은 물고기 수 증가
    if shark_eat == shark_size: 
        shark_size += 1 # 아기상어 크기증가
        shark_eat = 0  # 먹은 물고기 수 초기화
    shark_x, shark_y = fish_x, fish_y # 상어 위치이동

print(time)
