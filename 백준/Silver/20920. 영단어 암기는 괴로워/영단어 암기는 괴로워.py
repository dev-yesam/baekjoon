# 20920

# sys 모듈 사용
import sys


# 입력
n, m = map(int, sys.stdin.readline().split())


# 딕셔너리에 m 이상의 단어와 개수 쌍 추가
words = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        if word not in words:
            words[word]=1
        else:
            words[word]+=1

# 정렬
final = sorted(words.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))


# 출력
for i in final:
    print(i[0])



