
# 알쏭달쏭 백트래킹

N, M = map(int, input().split())  # N과 M을 입력받는다.

visited = [False] * (N + 1)  # 각 인덱스에 해당하는 숫자가 수열에 사용되었는지를 체크하는 리스트. 
output = [0] * M  # 최종적으로 출력할 수열을 저장하는 리스트.

def dfs(depth, N, M):  # 깊이 우선 탐색을 진행하는 재귀 함수. depth는 현재까지 수열에 포함된 숫자의 수입니다.
    if depth == M:  # 현재까지 수열에 포함된 숫자의 수가 M과 같으면,
        print(*output)  # output 리스트에 저장된 수열을 출력
        return
    for i in range(1, N + 1):  # i를 1부터 N까지
        if not visited[i]:  # i번째 숫자가 아직 수열에 사용되지 않았다면,
            visited[i] = True  # i번째 숫자를 수열에 사용했다는 표시를 합니다.
            output[depth] = i  # output 리스트의 depth번째 위치에 i를 넣습니다.
            dfs(depth + 1, N, M)  # 다음 depth의 탐색을 진행
            visited[i] = False  # 재귀 호출이 끝나면 i번째 숫자를 다시 사용하지 않았다는 표시. 이는 다른 수열을 만들 때 i를 재사용하기 위함

dfs(0, N, M)  # 최초로 dfs 함수를 호출하여 탐색을 시작합니다. 처음에는 아무 숫자도 수열에 포함되지 않았으므로 depth는 0입니다.

# ??????

'''
visited: [False, False, False, False, False]
output: [0, 0]
visited: [False, True, False, False, False]
output: [1, 0]
visited: [False, True, True, False, False]
output: [1, 2]
visited: [False, True, False, True, False]
output: [1, 3]
visited: [False, True, False, False, True]
output: [1, 4]

visited: [False, True, False, False, False]
output: [2, 0]
visited: [False, True, True, False, False]
output: [2, 1]
visited: [False, True, False, True, False]
output: [2, 3]
visited: [False, True, False, False, True]
output: [2, 4]

visited: [False, False, True, False, False]
output: [3, 0]
visited: [False, True, True, False, False]
output: [3, 1]
visited: [False, False, True, True, False]
output: [3, 2]
visited: [False, False, True, False, True]
output: [3, 4]

visited: [False, False, False, True, False]
output: [4, 0]
visited: [False, True, False, True, False]
output: [4, 1]
visited: [False, False, True, True, False]
output: [4, 2]
visited: [False, False, False, True, True]
output: [4, 3]
'''

'''
      1
     / \
    2   3
   /     \
  3       4
 /   
4

      2
     / \
    1   3
   /     \
  3       4
 /   
4

      3
     / \
    1   2
   /     \
  2       4
 /   
4

      4
     / \
    1   2
   /   / 
  2   3
 /   
3

'''