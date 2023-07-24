import sys
from collections import defaultdict

def solution():
    N, M = map(int, sys.stdin.readline().split())
    words = [sys.stdin.readline().strip() for _ in range(N)]
    word_dict = defaultdict(int)

    for word in words:
        if len(word) >= M:
            word_dict[word] += 1

    sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word in sorted_words:
        print(word[0])

solution()
