def solution(x, n):
    answer = []               # 빈 리스트 생성
    for n in range(1, n+1):   # 1~n까지 범위 내 자연수 반복
        answer.append(x*n)    # x*n값 answer 리스트에 차례로 추가
    return answer             # answer 리스트 반환