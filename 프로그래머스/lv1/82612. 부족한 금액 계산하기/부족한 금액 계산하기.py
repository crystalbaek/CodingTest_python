def solution(price, money, count):
    cost = 0                         # 총비용 cost 변수 초기화
    for n in range(0, count+1):      # 0부터 count회까지 반복
        cost += price * n            # count회까지 이용한 각 price를 누적해서 총비용 cost 구하기 
    
    if money < cost:             # 만약 소지한 돈이 총비용보다 적다면,
        answer = cost - money    # 부족한 금액을 계산하여 answer에 저장
    else:
        answer = 0               # 남은 돈이 충분한 경우, answer를 0으로 설정
    return answer                  