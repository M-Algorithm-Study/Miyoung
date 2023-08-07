def solution(s, n):
    result = ''
    for char in s:
        if char == ' ':
            result += char
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
    return result
