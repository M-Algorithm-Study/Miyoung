N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

visited = [False] * N  # 숫자를 방문했는지를 체크하는 리스트
sequence = []  # 현재까지 선택된 숫자들의 시퀀스

def backtrack(depth):
    if depth == M:  # 원하는 길이만큼 숫자를 선택했다면 출력
        print(' '.join(map(str, sequence)))
        return

    for i in range(N):
        if not visited[i]:  # 해당 숫자를 아직 방문하지 않았다면
            visited[i] = True  # 숫자 방문 표시
            sequence.append(numbers[i])  # 시퀀스에 숫자 추가
            backtrack(depth + 1)  # 다음 숫자 선택을 위한 재귀 호출

            # 백트래킹
            visited[i] = False
            sequence.pop()

backtrack(0)
