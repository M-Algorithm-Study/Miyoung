# 입력으로 테스트 케이스의 개수를 받습니다.
N = int(input())

for _ in range(N):
    password = input()
    
    if 6 <= len(password) <= 9:
        print('yes')
    else:
        print('no')
