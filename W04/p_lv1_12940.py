# 최대공약수와 최소공배수

def solution(n, m):
    def gcd(n, m):
        return n if m == 0 else gcd(m, n % m)
    return [gcd(n, m), n * m // gcd(n, m)]

