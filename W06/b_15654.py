

N, M = map(int, input().split()) # N개의 숫자, M(수열의 길이)
numbers = sorted(list(map(int, input().split()))) # N개의 숫자를 입력 > 리스트에 저장 > 오름차순 정렬

visited = [False] * N  # 방문표시 ( 현재 조합에 사용되었는지 여부)
sequence = []  # 숫자 조합 저장

def backtrack(depth): # 깊이를 매개변수로 받아 깊이에 맞는 순서를 선택
    if depth == M:  
        print(' '.join(map(str, sequence))) # depth(깊이)가 M(수열의 길이)에 도달하면 squence(숫자조합)을 출력하고 종료
        return

    for i in range(N):
        if not visited[i]:  # 방문하지 않은 숫자
            visited[i] = True  # 조합에 사용되었다면 방문처리
            sequence.append(numbers[i])  # 숫자 조합에 추가
            backtrack(depth + 1)  # 재귀호출 > 다음 깊이의 숫자를 선택.

            visited[i] = False # 방문처리 초기화
            sequence.pop()     # 숫자 조합 초기화

backtrack(0)
