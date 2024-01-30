# 14247

import sys
input = sys.stdin.readline

# 입력
n = int(input())
heights = list(map(int, input().split()))
velocity = list(map(int, input().split()))

# 높이와 속도 묶기 및 속도 순 정렬
trees_zip = list(zip(heights, velocity))
trees_zip.sort(key= lambda x:x[1])


# n 일 동안 등산하며 나무 베기
sum_trees = 0
for i in range(n):
    now_tree = trees_zip[i][0] + (i * trees_zip[i][1]) 
    sum_trees += now_tree


# 출력
print(sum_trees)

