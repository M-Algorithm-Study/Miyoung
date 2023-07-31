N, M = map(int, input().split())

visited = [False] * (N + 1)  
output = [0] * M 

def dfs(depth, N, M):
    if depth == M:  
        print(*output)
        return
    for i in range(1, N + 1):
        if not visited[i]: 
            visited[i] = True 
            output[depth] = i 
            dfs(depth + 1, N, M)  
            visited[i] = False  

dfs(0, N, M)