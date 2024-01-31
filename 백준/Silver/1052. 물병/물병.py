# 1052


# N : 현재 가지고 있는 물병
# K : 최종적으로 K 이하의 물병 만들어야 함.
# B : 사야하는 물병 수 => 최저 구해야함.


# N, K 입력 받음
N, K = map(int, input().split())

# 가지고 있는 물병수 다 합치면, 2진수로 110 이렇게 표현 됨. 4리터 하나, 2리터 하나.
# 비트 연산 개수에 맞춰줘야 겠네.
# 1. 2진수에서 1의 개수 카운팅.(k보다 큰지)
cnt =0
B = 1

N2= N
while N > 0:
    if N & B :
        cnt +=1
        N -= B
    B *= 2


if cnt <= K :
    print(0)

# 2. K보다 많다면, 2진수 뒤에서 ...
else:
    B2 = 1
    cnt = cnt-K
    C2 = 0
    while N2 > B2:
        if N2 & B2:
            if cnt ==0:
                res=B2-C2
            else:
                C2 += B2


            cnt -= 1
        B2 *= 2


    print(res)

