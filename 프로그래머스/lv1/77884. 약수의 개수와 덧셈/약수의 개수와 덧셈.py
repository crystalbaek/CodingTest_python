def solution(left, right):
    answer = 0
    for i in range(left, right + 1):  # 두 정수 사이의 수 구하기
        count = 0
        for j in range(1, i + 1): 
            if i % j == 0: # 약수인 경우
                count += 1 # 약수의 수 구하기
                
        # 약수의 개수가 짝수면 더하고 홀수면 빼기
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer