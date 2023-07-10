n = input()
result = [ 0 for _ in range(n)]
p = 4
for i in range(n):
    RGB = list(map(int, input().split()))
    for j in range(len(RGB)):
        if result[i] < RGB[j]:
            if p != j:
                result[i] = RGB[j]
                p = j
print(min(result)) 

# 틀렸습니당