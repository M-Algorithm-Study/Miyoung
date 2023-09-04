'''
부분합(투포인터)
'''
N, S = map(int, input().split())
array = list(map(int, input().split()))

start, end, partial_sum = 0, 0, 0  # 시작, 끝 , 부분 합
min_length = int('inf')  # 최소 길이 (무한대로 초기화)

while end <= N:
    if partial_sum >= S:
        min_length = min(min_length, end - start)  # 최소 길이로 갱신
        partial_sum -= array[start]
        start += 1  # 시작 포인터를 오른쪽으로 이동
    elif end == N:
        break
    else:
        partial_sum += array[end] 
        end += 1  # 끝 포인터를 오른쪽으로 이동

if min_length == int('inf'):
    print(0)
else:
    print(min_length)
