from itertools import combinations

def solution(number):
    count = 0
    # 주어진 배열에서 3명의 학생을 선택하는 모든 조합 생성
    comb = combinations(number, 3)

    for c in comb:
        # 3명의 학생의 번호를 더해서 합을 계산
        total = sum(c)
        # 합이 0이면 삼총사로 인정하고 count를 증가
        if total == 0:
            count += 1

    return count