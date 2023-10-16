def solution(a, b):
    op_value = int(str(a) + str(b))
    mul_value = 2 * a * b

    return max(op_value, mul_value)