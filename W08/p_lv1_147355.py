def solution(t, p):
    p_value = int(p)
    p_len = len(p)
    
    count = 0
    for i in range(len(t) - p_len + 1):  
        sub_str = t[i:i+p_len]  
        if int(sub_str) <= p_value: 
            count += 1

    return count