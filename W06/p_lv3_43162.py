# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def dfs(computers, visited, v): # dfs(깊이 우선 탐색) coumputers(2차원 리스트. 컴퓨터간의 연결상태), visited 방문 여부를 담은 1차원 리스트, v(현재 방문하고 있는 인덱스)
    visited[v] = True # 방문표시
    for i in range(len(computers)): # 컴퓨터 순회
        if computers[v][i] == 1 and visited[i] == False:  # 하나로 연결되어 있고, 방문을 하지않았다면 (1 연결, 0 비연결)
            dfs(computers, visited, i) # 재귀함수로 dfs 순회
    
def solution(n, computers): 
    answer = 0  # 네트워크 갯수
    visited = [False] * n # 방문 여부 배열 생성
    for i in range(n):
        if visited[i] == False: # 방문하지 않았다면
            dfs(computers, visited, i) # dfs실행. solution i는 dfs의 v로 전달된다.
            answer += 1  # dfs가 실행 될때마다 +1
    return answer # 네트워크 갯수 반환 

# print(solution(n, computers))
