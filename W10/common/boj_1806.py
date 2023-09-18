'''
부분합(투포인터)
'''
N, S = map(int, input().split())
array = list(map(int, input().split()))

start, end, partial_sum = 0, 0, 0  # 시작, 끝 , 부분 합
min_length = int('inf')  # 최소 길이 (무한대로 초기화)

while end <= N: # end포인터가 끝까지 가면 종료
    if partial_sum >= S: # 부분합 >= S
        min_length = min(min_length, end - start)  # 현재 부분합과 이전의 부분합(end-start) 중 최소 길이로 갱신, 
        # 포인터 이동전에 갱신
        partial_sum -= array[start] # 시작포인터 빼고
        start += 1  # 시작 포인터를 오른쪽으로 이동
    elif end == N: # end 포인터가 끝까지 도달
        break
    else: # 부분합이 S보다 작고 end가 배열끝에 도달하지 않으면
        partial_sum += array[end] # end 포인터
        end += 1  # 끝 포인터를 오른쪽으로 이동

if min_length == int('inf'): # S 이상 되는 것이 없다면
    print(0)
else:
    print(min_length)
