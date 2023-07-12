# 1.
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += (i)
    return answer

# 2.
def solution(n):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# 3.
def solution(n):
    divisor_list = []
    
    for i in range(1, n+1):
        if n % i == 0:
            divisor_list.append(i)

    answer = sum(divisor_list)
    return answer