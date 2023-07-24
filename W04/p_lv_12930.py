# 이상한 문자 만들기
def solution(s):
    return ' '.join([''.join([char.upper() if idx % 2 == 0 else char.lower() for idx, char in enumerate(word)]) for word in s.split(' ')])
