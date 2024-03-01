# L 개의 알파벳으로 암호가 구성됨
# 최소 1개의 모음(aeiou)과 최소 2개의 자음
# 암호 알파벳 오름차순
# C 개의 가능한 암호 수

# 모음 자음 리스트에서 n 개 뽑는 함수
# 백트래킹
def cmb(level, start, cnd_lst, vclst, n):
    if level == n:
        cnd_lst.append(cmb_lst[:])
        return

    # 재귀 호출
    for i in range(start, len(vclst)):
        cmb_lst.append(vclst[i])
        cmb(level+1, i+1, cnd_lst, vclst,n)
        cmb_lst.pop()




# 입력
L, C = map(int, input().split())

# C 개 중에서,
# 모음 1개 , 자음 L-1 개
# 모음 2개 , 자음 L-2 개
# ...
# 모음 L-2개, 자음 2개

# C 입력 받아 모음 자음 분할
vowel_lst = ['a', 'e', 'i', 'o', 'u']
lst = input().split()
vowels = []
cons = []
for character in lst:
    if character in vowel_lst:
        vowels.append(character)
    else:
        cons.append(character)


# 모음 개수별로 조합으로 뽑은 다음 오름차순 돌리기
total = []
for q in range(1, min(L - 1, len(vowels)+1)):

    # 뽑은 모음
    vow_cnd =[] # 모음 후보군
    cmb_lst = []
    cmb(0, 0,vow_cnd, vowels, q)


    # 뽑은 자음
    con_cnd = [] # 자음 후보군
    cmb_lst = []
    cmb(0, 0, con_cnd, cons, L-q)

    # 자음 모음 후보군 각각 마다 출력

    for vow in vow_cnd:
        for con in con_cnd:
            n = vow+con
            n.sort()
            n = ''.join(n)
            total.append(n)

total.sort()
for t in total:
    print(t)

