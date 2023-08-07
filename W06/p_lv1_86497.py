def solution(sizes):
    max_long = max(max(size) for size in sizes)
    max_short = max(min(size) for size in sizes)
    return max_long * max_short