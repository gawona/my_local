c = int(input()) # 리스트 개수
a = [] # n + score list
for i in range(c) :
    a.append(list(map(int, input().split())))
lst = []
for i in range(c):
    n = a[i].pop(0) # 학생 수 
    # print(sum(int(a[i])))
    sum = 0
    for j in range(int(n)):
        sum += a[i][j]
    avg = sum / n

    # print(f"{}")
    #     lst.append(a[i][j])

# print(lst)
# print((map(int,a)))
