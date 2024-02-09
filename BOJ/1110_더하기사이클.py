N = str(input())    # 입력 받은 정수를 str로 저장
if int(N) < 10:     # N이 10보다 작으면, 앞에 0 붙여 저장
    N = '0' + N
init = N            # 처음 입력 받은 정수 저장
cnt = 0             # 사이클 길이 세는 변수
while True:
    num = 0         # 정수의 각 자리 합 저장할 변수
    digit = int(N) % 10
    for s in N:     # 정수의 각 자리 합 구하기
        num += int(s)
    num_digit = num % 10
    N = str(digit) + str(num_digit)
    cnt += 1        # 사이클 길이 1 증가
    if N == init:   # 처음 입력 받은 정수와 같으면
        print(cnt)  # 사이클 길이 출력하고
        break       # while문 탈출
