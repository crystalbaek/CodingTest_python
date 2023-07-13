def solution(s):
    s = s.lower() # 소문자로 통일하기 위해 문자열을 소문자로 변환
    if s.count('p') == s.count('y'):
        answer = True
    elif s.count('p') != s.count('y'):
        answer = False
    else:
        answer = True
    return answer