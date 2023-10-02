

n, k = map(int, input().split()) # n 가위질 횟수, k 만들고 싶은 색종이 조각의 개수
left = 0
right = n // 2
is_possible = False

while left <= right:
    row_cut = (left + right) // 2 # 가로로 자를 횟수
    col_cut = n - row_cut  # 세로로 자를 횟수
    pieces = (row_cut + 1) * (col_cut + 1) # 만든 조각의 개수
    if k == pieces:   
        print('YES')  # 만든 조각의 개수가 k와 같다면  YES
        is_possible = True
        break
    if k > pieces:   # 만든 조각의 개수가 k보다 작다면
        left = row_cut + 1   # left 인덱스를 오른쪽으로 이동
    else:
        right = row_cut - 1  # right 인덱스를 왼쪽으로 이동

if not is_possible:  # 결과가 없다면 NO 출력
    print('NO')
