def solution(n, m):
    answer = []
    # 최대공약수를 구하기 위해 두 수 중 작은 값까지만 반복합니다.
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            maxnum = i
    # 최소공배수를 구하기 위해 두 수를 최대공약수로 나눈 값을 계산합니다.
    minnum = (n * m) // maxnum
    answer.append(maxnum)
    answer.append(minnum)
    return answer