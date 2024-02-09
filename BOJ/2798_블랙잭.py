N, M = map(int, input().split())
cards = list(map(int, input().split()))

def comb(n, r):
    if r == 0 or n == r:
        return 1
    return comb(n-1, r-1) + comb(n-1, r)

comb_lst = []
for n in range(N):
    if comb(n, 3) <= M:

