def solution(n):
    sorted_str = "".join(sorted(str(n), reverse=True))
    # 정수 n을 문자열로 변환하고, 문자열을 내림차순으로 정렬한 후 각 문자를 연결하여 하나의 문자열로 만듦
    answer = int(sorted_str)
    # 정렬된 문자열을 정수로 변환
    return answer
