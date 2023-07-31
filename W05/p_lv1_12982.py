def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if budget - i >= 0:
            budget -= i
            count += 1
        else:
            break
    return count