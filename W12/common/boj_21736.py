# 캠퍼스의 크기를 나타내는 두 정수 
# 캠퍼스의 정보
# O는 빈 공간, X는 벽, I는 도연이, P는 사람

from collections import deque

# 상, 하, 좌, 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, campus):
    count = 0  # 만난 사람 수
    visited = [[False]*m for _ in range(n)] # 방문 여부
    queue = deque([(x, y)]) # 초기값 도연이 위치
    visited[x][y] = True # 방문 표시

    while queue:
        x, y = queue.popleft()

        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i] # 상 하 좌 우

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # 영역 내에 있고 방문하지 않았다면
                visited[nx][ny] = True # 방문표시

                if campus[nx][ny] == 'P': # 사람이라면
                    count += 1  # 만난 사람 수 증가
                    queue.append((nx, ny)) # 큐에 추가
                elif campus[nx][ny] == 'O': # 빈 공간이라면
                    queue.append((nx, ny)) # 큐에 추가

    return count # 만난 사람 수

n, m = map(int, input().split()) # 캠퍼스 크기
campus = [list(input().strip()) for _ in range(n)] # 캠퍼스 정보

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I': # 도연이라면
            start_x, start_y = i, j # 도연이 위치 저장
            break

result = bfs(start_x, start_y, campus) # 만난 사람 수

if result == 0: 
    print("TT") # 만난 사람 수가 0이면 TT
else:
    print(result)
