def solution(food):
    answer = ''
    for i in range(1,len(food)):  # 1부터 (food 리스트 길이 - 1)까지 반복
        answer += str(i)*(food[i]//2)
        # i번째 인덱스에 해당하는 값의 절반만큼, i를 문자열로 변환하여 answer에 추가
    temp = ''.join(reversed(list(answer)))  # answer에 대해 역순으로 재배열
    
    return answer+'0'+temp
    # 결과 문자열을 구성하기 위해 answer+'0'+temp를 반환
    # 가운데에 0을 추가하여 문자열을 완성