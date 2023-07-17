def solution(arr, divisor):
    answer = []  # 결과를 저장할 빈 리스트를 생성

    # 주어진 배열의 각 요소를 반복-> 나누어 떨어지는지 확인
    for n in arr:
        if n % divisor == 0:  # 현재 요소가 divisor로 나누어 떨어지면
            answer.append(n)  # 결과 리스트에 해당 요소를 추가

    if answer == []:  # 결과 리스트가 비어있다면 (나누어 떨어지는 요소가 없다면)
        return [-1]  # -1을 원소로 갖는 리스트를 반환
    else:
        return sorted(answer)  # 결과 리스트를 오름차순으로 정렬하여 반환