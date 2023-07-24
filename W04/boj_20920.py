import sys
from collections import defaultdict # 존재하지 않는 키를 조회할 경우에 에러를 발생시키는 대신 기본값을 반환하는 딕셔너리의 서브클래스

def solution():
    N, M = map(int, sys.stdin.readline().split()) # 총 단어갯수, M 길이 이상의 단어만 외운다.
    words = [sys.stdin.readline().strip() for _ in range(N)]
    word_dict = defaultdict(int) # 딕셔너리 기본값 0

    for word in words:
        if len(word) >= M:
            word_dict[word] += 1
    # 리스트의 각 단어에 대해, 단어의 길이가 M 이상일 경우 해당 단어의 빈도수를 증가
    sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # 빈도수가 높은 순, 단어의 길이가 긴 순, 알파벳 순서가 앞선 순서로 정렬

    for word in sorted_words:
        print(word[0])

solution()
