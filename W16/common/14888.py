n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 덤셈, 뺄셈, 곱셈, 나눗셈

max_val = -float('inf') # 음의 무한대
min_val = float('inf')  # 양의 무한대

def dfs(depth, total, add, sub, mul, div):
    global max_val, min_val
    if depth == n: # 모든 수를 사용 했을 경우
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    if add > 0: 
        dfs(depth + 1, total + nums[depth], add - 1, sub, mul, div)
    if sub > 0:
        dfs(depth + 1, total - nums[depth], add, sub - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, total * nums[depth], add, sub, mul - 1, div)
    if div > 0:
        if total < 0:
            dfs(depth + 1, -(-total // nums[depth]), add, sub, mul, div - 1)
        else:
            dfs(depth + 1, total // nums[depth], add, sub, mul, div - 1)

dfs(1, nums[0], add, sub, mul, div)
print(max_val)
print(min_val)
