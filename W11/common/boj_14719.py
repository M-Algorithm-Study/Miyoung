# H, W = 4, 8
# blocks = [ 3, 1, 2, 3, 4, 1, 1, 2 ]

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

left_max = [0] * W
right_max = [0] * W

max_height = 0
for i in range(W):
    max_height = max(max_height, blocks[i])
    left_max[i] = max_height

max_height = 0
for i in range(W-1, -1, -1):
    max_height = max(max_height, blocks[i])
    right_max[i] = max_height

total_water = 0
for i in range(W):
    total_water += min(left_max[i], right_max[i]) - blocks[i]

print(total_water)


'''
  min
  ⌒ ⌒ ⌒ ⌒ ⌒ ⌒ ⌒ ⌒
  3 3 3 3 4 4 4 4
  4 4 4 4 4 2 2 2
  ⏝ ⏝ ⏝ ⏝ ⏝ ⏝ ⏝
- 3 1 2 3 4 1 1 2
-----------------
  0 2 1 0 0 1 1 0
'''