def solution(s):
    result = []
    for s in s.split(' '):  #띄어쓰기를 기준으로 문자를 분리해준다.
        st = ''
        for i in range(len(s)):  #index를 생성해주기 위해 for문을 만들어준다.
            if i % 2 == 0:  #짝수번째라면 대문자, 홀수번째라면 소문자
                st += s[i].upper()  #그 결과는 st라는 새로운 공간에 붙여준다.
            else :
                st += s[i].lower()
        result.append(st)  #변형시킨 st들을 result에 리스트로 붙여준다.
    return ' '.join(result)  #띄어쓰기를 기준으로 다시 문자를 붙여준다.

# 다른풀이
def solution(s):
    answer = ''
    arr = s.split(' ')
    for s in arr:
        for i, x in enumerate(s):
            answer += x.upper() if i % 2 == 0 else x.lower()
        answer += ' '
    return answer[:-1]