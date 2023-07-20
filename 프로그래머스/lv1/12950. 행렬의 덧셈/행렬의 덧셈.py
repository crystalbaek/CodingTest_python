def solution(arr1, arr2):
    answer = arr1  # arr1을 answer에 할당
    
    # arr1과 arr2의 각 요소들을 더해서 answer 배열에 저장
    for i in range(len(arr1)):  # 행의 길이만큼 반복
        for j in range(len(arr1[i])):  # 열의 길이만큼 반복
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer