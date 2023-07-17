
# & and
# ~ not
# | or
# << 왼쪽 시프트 연산자. 2진수로 만들어 왼쪽으로 밀어버리고 0을 채워서 값을 반환한다  4 << 1 면 100(4)이 1000(8)으로 되어서 2배가 된다.
# >> 오른쪽 시프트 연산자. 4 >> 1 

def solve(i, left, right, middle):
    global answer, mask
    valid = mask & ~(left | right | middle)
    while valid:
        pos = valid & (-valid)
        valid = valid & (valid - 1)
        if i != n - 1:
            solve(i + 1, (left | pos) << 1, (right | pos) >> 1, middle | pos)
        else:
            answer += 1

n = int(input())
answer = 0
mask = (1 << n) - 1
solve(0, 0, 0, 0)
print(answer)