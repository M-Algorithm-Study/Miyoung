# 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)
# 고장난 버튼의 개수 M (0 ≤ M ≤ 10)
# 고장난 버튼

def possible(channel, broken): # 채널번호, 고장난 버튼 목록
    if channel == 0:
        if 0 in broken: # 고장난 버튼에 0
            return False
        return True
    while channel > 0: 
        if channel % 10 in broken: # 마지막 숫자가 버튼에 포함되어있는지
            return False
        channel //= 10 # 마지막 숫자를 제거
    return True

n = int(input()) # 수빈이가 이동하려고 하는 채널
m = int(input()) # 고장난 버튼의 개수
broken = set()
if m > 0:
    broken = set(map(int, input().split())) # 고장난 버튼

answer = abs(n - 100) # 최소 버튼 클릭 횟수, 100 부터 시작

for i in range(1000001): # 브루트포스
    if possible(i, broken): # i 채널을 누를 수 있다면
        answer = min(answer, len(str(i)) + abs(i - n)) # 더 작은값

print(answer)
