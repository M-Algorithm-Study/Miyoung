n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)] # 2차원 리스트로 저장

dx = [-1, 1, 0, 0] # 위 아래 변경값을 저장
dy = [0, 0, -1, 1] # 좌 우 변경값을 저장

def dfs(x, y): # 깊이 우선 탐색 start
    global count # count를 전역변수로 선언
    graph[x][y] = 0 # 현재 방문한 위치의 값을 0으로 변경
    count += 1  # 연결된 집의 수 +1
    for i in range(4):  
        # 1.   위(dx[0], dy[0]) 
        # 2.  아래(dx[1], dy[1]) 
        # 3.  왼쪽(dx[2], dy[2]) 
        # 4. 오른쪽(dx[3], dy[3])
        nx = x + dx[i] 
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n: 
            # 해당 좌표가 그리드 내부에 있고
            # nx >= 0: 위 (0 부터)
            #nx < n: 아래 (n-1 까지)
            # ny >= 0: 왼쪽 (0 부터)
            # ny < n: 오른쪽 (n-1 까지)
            if graph[nx][ny] == 1: # 위치 값이 1인 경우 dfs를 재귀적으로 호출. 연결된 무든 집을 탐색
                dfs(nx, ny)

result = []  # 단지의 수
for i in range(n):      #
    for j in range(n):  # n * n 모든 집을 순회
        if graph[i][j] == 1: #  아직 방문하지 않은 집이면 DFS 시작
            count = 0        #  새로운 단지의 연결된 집의 수를 세기위해 초기화
            dfs(i, j)        # 해당 집에서 시작하여 연결된 모든 집을 DFS로 탐색
            result.append(count) # 단지의 집수를 리스트에 추가.

print(len(result))  # 찾아낸 그룹의 수를 출력
for r in sorted(result):  # 리스트를 오름차순으로 정렬, 작은 순서대로 출력.
    print(r)