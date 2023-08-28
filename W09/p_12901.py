def solution(a, b):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    total_days_passed = sum(days_in_month[:a-1]) + b - 1

    return days_of_week[total_days_passed % 7]

# 예제
a = 5
b = 24
print(solution(a, b))  # "TUE"
