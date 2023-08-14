def solution(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd
        sliced_array = array[i-1:j]  
        sliced_array.sort()
        answer.append(sliced_array[k-1])
    return answer