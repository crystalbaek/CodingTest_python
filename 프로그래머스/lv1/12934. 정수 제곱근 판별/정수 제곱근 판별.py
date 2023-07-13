def solution(n):
    x = int(n**(1/2))          # x는 n의 제곱근
    if n == x**2:         # 만약 n이 x의 제곱이라면 
        answer = (x+1)**2 
    else:
        answer = -1
    return answer