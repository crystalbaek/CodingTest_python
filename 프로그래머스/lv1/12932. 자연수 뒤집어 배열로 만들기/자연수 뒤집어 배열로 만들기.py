# 1.
def solution(n):
    answer = []                # 빈 리스트 
    s = reversed(str(n))       # 숫자 n을 뒤집은 순서로 순회하는 이터레이터
    for i in s:                # for 루프로 s를 반복
        answer.append(int(i))  # 각 자릿수를 정수로 변환하여 리스트로 저장
    return a

# 2. 
def solution(n):
	return [int(i) for i in str(n)][::-1]

# n을 문자열로 변환 후, 각 문자를 정수로 변환하여 리스트로 만들기, [::-1] : 역순으로 리스트 저장 

# 3. 
def solution(n):
	return list(map(int, reversed(str(n))))

# 1) reversed(): 숫자 n을 뒤집은 순서로 순회하는 이터레이터를 생성
# 2) map(): 각 자릿수를 정수로 변환 -> reversed() 이터레이터를 인자로 전달합니다.
# 3) return list(): 뒤집힌 리스트 반환
