# 0 -> 2 -> 4-> 8 -> 16 ->
# 2x2, 4x4, 8x8, 16x16

# 1. 처음에 행, 열의 그자체의 숫자를 계산 해보자.

# 2. 지수 (exponent)
# 0, 4-> 4이상인게 존재하네? -> 16의 배수를 더해주는 거네
# 16의 몇배를 더해줄거야? 행 일때 열 일때? 두개 다일때. 3가지 조건이야
# c -> 1배 r -> 2배 c, r -> 3배
# 
# 0 1 
# 2 3 만 주어줄건데. 이것의 배수가 아니면 어쩔래?
# 예를 들어 4,2 -> 16의 1배수를 더하는거네
# 근데 열의 수만 4이상이니깐.  열만 2로 나누자. 그것의 16의 1배를 더하면 돼
# 어..? 근데 없네? 그러면 얘도 다시 계산해봐 -> 재귀 특성
# 


def getResult(r, c):
    # 둘다 1보다 작으면
    if r <=1 and c <=1:
        return r*2 + c
    else:
        cr = r
        cc = c
        rcount = 0
        ccount = 0
        while cr//2 > 0:
            cr //= 2
            rcount += 1
        while cc//2 > 0:
            cc //= 2
            ccount += 1
        # 더 큰 지수를 찾자
        if ccount > rcount:
            expo = ccount
        else:
            expo = rcount
        

        # 몇을 더 할지를 알아봐야지
        plus = (4**(expo))
        m = 2**expo
        # plus의 몇 배를 더할 것이냐 조건 세개
        # 1. 둘다 2**expo보다 크거나 같다
        if r >= m and c >= m:
            return 3*plus + getResult(r-m, c-m)
        elif r >= m:
            return 2*plus + getResult(r-m, c)
        else:
            return plus + getResult(r, c-m)

        
    
N, r, c = [int(i) for i in input().split()]
print(getResult(r, c))