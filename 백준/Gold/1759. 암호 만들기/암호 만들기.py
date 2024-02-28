# L 암호 수
# C 가능성 있는 문자 수
# aeiou 1개 이상, 자음 2개 이상
L, C = map(int, input().split())
lst = list(input().split())
vowels_lst = ['a', 'e', 'i', 'o', 'u']
vow = []
con = []
for char in lst:
    if char in vowels_lst:
        vow.append(char)
    else:
        con.append(char)

final = []
for vow_num in range(1, L - 1):
    con_num = L - vow_num


    # 조합 함수
    def comb(level, goal, start, lst, password, num, vow_con):
        if level == goal:
            password.append(lst[:])
            return

        for i in range(start, num):
            lst.append(vow_con[i])
            comb(level + 1, goal, i + 1, lst, password, num, vow_con)
            lst.pop()


    ## 모음에서 vow_num 개 뽑고,
    vow_pass = []
    temp1 = []
    comb(0, vow_num, 0, temp1, vow_pass, len(vow), vow)
    ## 자음에서 con_num 개 뽑고,
    con_pass = []
    temp2 = []
    comb(0, con_num, 0, temp2, con_pass, len(con), con)

    ## 두개 for문으로 곱해준 후에 정렬하고 출력
    # 최종

    for i in vow_pass:
        for j in con_pass:
            password = []
            password.extend(i)
            password.extend(j)
            password.sort()
            final.append(''.join(password))

# 출력
final.sort()
for i in final:
    print(i)