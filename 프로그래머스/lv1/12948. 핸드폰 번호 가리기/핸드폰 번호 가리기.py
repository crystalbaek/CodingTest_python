def solution(phone_number):
    answer = '*' * (len(phone_number) - 4)
    # 전체 길이에서 마지막 네 자리를 제외한 길이만큼 '*'를 생성하여 앞부분을 대체
    # answer = phone_number[:-4].replace('*', '*') 가능
    answer += phone_number[-4:]
    # 마지막 네 자리를 그대로 answer에 붙임
    return answer
