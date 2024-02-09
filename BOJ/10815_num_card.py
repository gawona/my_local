N = int(input())                            # N : 카드 개수
cards = set(map(int, input().split()))      # 카드에 적힌 정수 리스트 (중복 x)
M = int(input())                            # M : 정수 개수
numbers = list(map(int, input().split()))   # M 개의 정수 리스트

ex_lst = []                     # 존재 여부 저장 리스트
for num in range(M):            # numbers 의 정수 모두 접근
    if numbers[num] in cards:   # cards 의 카드 모두 접근
        ex_lst.append(1)
    else:
        ex_lst.append(0)

print(*ex_lst)