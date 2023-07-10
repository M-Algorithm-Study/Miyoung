def solution():
    arrangement = input().strip()
    stack = []  # 쇠막대기를 임시로 저장하기 위한 스택
    answer = 0  # 잘린 쇠막대기 조각의 개수를 저장한 변수

    for i in range(len(arrangement)):  # 입력받은 문자열의 각 문자에 대해 반복
        if arrangement[i] == '(':  # 현재 문자가 여는 괄호인 경우
            stack.append('(')      # 여는 괄호를 만나면, 쇠막대기의 시작을 의미하므로 스택에 추가
        else:  # 현재 문자가 닫는 괄호인 경우
            if arrangement[i-1] == '(':  # 바로 앞의 문자가 여는 괄호인 경우 (레이저)
                stack.pop()  # 레이저를 스택에서 제거
                answer += len(stack)
            else:  #  바로 앞의 문자가 여는 괄호가 아닌 경우 (쇠막대기의 끝)
                stack.pop()  # 쇠막대기의 끝을 스택에서 제거
                answer += 1  # 쇠막대기의 마지막 부분이므로, 조각의 개수를 1개 추가

    print(answer)

solution()