import sys; sys.stdin = open('input.txt')

N = int(input())    # N 개의 단어
# 1. 길이가 짧은 것부터 정렬
# 2. 길이가 같으면 사전 순으로 정렬
# 조건 : 중복 단어 제거
word_lst = []       # 단어 리스트
len_lst = []        # 단어 길이 저장 리스트

# 단어 입력 받아 word_lst, len_lst 생성
for n in range(N):
    word = input()
    word_lst.append(word)
    len_lst.append(len(word))

# 길이 순으로 word_lst 내 단어 정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if len_lst[j] > len_lst[j+1]:
            len_lst[j], len_lst[j+1] = len_lst[j+1], len_lst[j]
            word_lst[j], word_lst[j+1] = word_lst[j+1], word_lst[j]

# word_lst 내 중복 단어 제거
one_word = []
for word in word_lst:
    if word not in one_word:
        one_word.append(word)

# print(one_word)
# one_lst 길이 같은 단어 사전순 정렬
# sort_lst = []
for w in range(len(one_word)-1):
    if len(one_word[w]) == len(one_word[w+1]):
        # sort_lst.append(one_word[w])
        # sort_lst.append(one_word[w+1])
        if one_word[w] > one_word[w+1]:
            one_word[w], one_word[w+1] = one_word[w+1], one_word[w]
        # sort_lst.sort()
for w in range(len(one_word)-1):
    if len(one_word[w]) == len(one_word[w+1]):
        if one_word[w][0] == one_word[w+1][0]:
            if one_word[w][1] > one_word[w+1][1]:
                one_word[w], one_word[w+1] = one_word[w+1], one_word[w]

for word in one_word:
    print(word)