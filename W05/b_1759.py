from itertools import combinations # 주어진 목록에서 특정 수(L개)의 항목을 선택하여 만들 수 있는 모든 가능한 그룹을 찾아준다.

vowels = ('a', 'e', 'i', 'o', 'u') 
l, c = map(int, input().split())

array = sorted(list(map(str, input().split())))

for password in combinations(array, l): # L개의 모든 문자 조합을 생성
    count = 0
    for i in password:
        if i in vowels:
            count += 1  # i 가 모음이면 1 증가
    if count >= 1 and count <= l - 2:
        print(''.join(password))  # 모음이 1 이상이고 자음이 2 이상이면 출력