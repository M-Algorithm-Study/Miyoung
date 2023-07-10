def solution(sequence, k):
    start = 0
    end = 0
    current_sum = sequence[0]
    result = [0, len(sequence)-1]

    while end < len(sequence):
        if current_sum == k:
            if end - start < result[1] - result[0]:
                result = [start, end]
            current_sum -= sequence[start]
            start += 1
        elif current_sum < k:
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else: 
            current_sum -= sequence[start]
            start += 1
            
    return result