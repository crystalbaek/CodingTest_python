def solution(numbers):
    l=len(numbers)
    answer = []
    index=0
    for i in range(l-1): # 모든 가능한 덧셈 조합을 구하기 위해, 두 개의 숫자 선택
        for j in range(i+1, l):
            answer.append(numbers[i] + numbers[j])
            
    answer=list(set(answer)) # 중복된 값을 제거하기 위해 set으로 변환한 뒤 다시 리스트로 변환
    answer.sort() # 오름차순 정렬
    return answer