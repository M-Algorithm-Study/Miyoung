# T를 S로 바꾼다. 과정은 반대, 결과는 같다.
S = input().strip()
T = input().strip()

while len(T) > len(S):
    if T[-1] == 'A':    
        T = T[:-1]    # T의 마지막 문자가 A라면 A를 제거
    elif T[-1] == 'B':   # 마지막 문자가 B라면
        T = T[:-1]   # B를 제거
        T = T[::-1]    # 문자열 뒤집기

# 최종 결과 출력
print(1 if S == T else 0)
