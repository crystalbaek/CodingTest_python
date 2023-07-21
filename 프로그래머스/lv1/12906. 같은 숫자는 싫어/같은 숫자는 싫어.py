def solution(arr):
    answer = [arr[0]]  # 결과를 담을 리스트 초기화, 첫 번째 요소를 추가
    for i in range(1, len(arr)):  # 인덱스 1부터 시작하여 배열을 순회
        if arr[i] != arr[i-1]:  # 현재 요소가 이전 요소와 다른 경우에만 실행
            answer.append(arr[i])  # 현재 요소를 결과 리스트에 추가
    return answer  

# 빈 배열 만들고 [0] 인덱스 넣어준 후 그 다음 숫자부터는 전 인덱스랑 비교해서 다르면 새 열에 넣어주기.