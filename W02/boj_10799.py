def solution():
    arrangement = input().strip()
    stack = []
    answer = 0

    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
        else:
            if arrangement[i-1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1

    print(answer)

solution()