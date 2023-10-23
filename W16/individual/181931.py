def solution(a, d, included):
    result = 0
    for i, include in enumerate(included):
        if include:
            result += a + d * i
    return result