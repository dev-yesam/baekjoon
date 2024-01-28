
# 입력 받기
import sys

n = int(sys.stdin.readline())
lst = []  # 책을 담을 리스트
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

max_book_index = lst.index(n)
max_book = n
for i in lst[:max_book_index][::-1]:
    if i == max_book-1:
        max_book= i
    else:
        pass
print(max_book-1)