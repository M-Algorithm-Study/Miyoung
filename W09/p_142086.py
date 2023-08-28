def solution(s):
    last_occurrence = {}  
    result = []  
    
    for i, char in enumerate(s):
        if char in last_occurrence:
            result.append(i - last_occurrence[char])
        else:
            result.append(-1)
        last_occurrence[char] = i 

    return result