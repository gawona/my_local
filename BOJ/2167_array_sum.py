from sys import stdin

N, M = map(int, stdin.readline().split())   # 배열 크기 N x M
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

K = stdin.readline()        # 줄 수
K_arr = [list(map(int, stdin.readline().split())) for _ in range(K)]

