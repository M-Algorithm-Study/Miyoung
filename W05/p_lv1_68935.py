def solution(n):
    answer = 0
    temp = ''

    while n:
        n, remainder = divmod(n, 3)
        temp += str(remainder)

    answer = int(temp, 3)
    
    return answer