from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [0] * MAX
    queue = deque([n])

    while queue:
        current = queue.popleft()
        
        if current == k:  # 동생을 찾았다면
            return visited[current]
        
        # 걷기 (current - 1)
        if 0 <= current - 1 < MAX and not visited[current - 1]:
            visited[current - 1] = visited[current] + 1
            queue.append(current - 1)
        
        # 걷기 (current + 1)
        if 0 <= current + 1 < MAX and not visited[current + 1]:
            visited[current + 1] = visited[current] + 1
            queue.append(current + 1)
        
        # 순간이동 (current * 2)
        if 0 <= current * 2 < MAX and not visited[current * 2]:
            visited[current * 2] = visited[current] + 1
            queue.append(current * 2)
            
    return -1

n, k = map(int, input().split())
print(bfs(n, k))
