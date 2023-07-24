def solution(number):
    answer = 0
    # 세 개의 숫자를 선택하는 모든 조합을 구하기 위한 세 개의 중첩된 반복문
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                # 세 개의 숫자를 더하여 합이 0인지 확인
                if number[i] + number[j] + number[k] == 0:
                    # 합이 0이라면 정답 카운터를 1 증가시킴
                    answer += 1
    # 모든 경우를 검사한 뒤, 합이 0인 경우의 개수를 반환
    return answer