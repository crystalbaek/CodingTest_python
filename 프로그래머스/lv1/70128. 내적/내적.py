def solution(a, b):
    n = len(a)    # 배열의 크기를 n으로 지정하기
    answer = 0    # 결과를 담을 변수를 초기화
    for n in range(0, n):   # 리스트의 각 요소에 접근하기 위해 반복문을 실행
        answer = answer + (a[n]*b[n])    # 리스트 a와 b의 요소를 각각 곱하여 결과에 더하기
    return answer