import sys
sys.stdin = open("input.txt")

T = int(input())

def goFloor(big_idx, small_idx, big_floor, small_floor):
    # 아래에서 위로 올라갈 수록 갈 수 있는 수의 범위가 넓어짐 -> 역삼각형 형태 !
    # 범위는 아래층의 idx보다 작은 것들만 포함하지 위층 idx가 더 클 경우 더 가야함
    # 넓어지는 범위는 아래와 위의 층차이 만큼 넓어진다 !
    result = big_floor - small_floor
    if big_idx < small_idx:
        result += small_idx - big_idx
    else:
        floor_diff = big_floor - small_floor
        if big_idx - floor_diff > small_idx:
            result += big_idx - floor_diff - small_idx

    return result

for tc in range(1, T+1):
    # a, b 각 층을 구한다.
    # while 문을 돌려서 피라미드 오른쪽이 a, b보다 크거나 같은 지점이 도착! 그러면 나는 이 층이야
    a, b = map(int, input().split())
    
    # 1층의 마지막점, next는 다음 층의 마지막점으로 가기 위해 더해야하는 수, floor는 현재 층
    # max 두 수는 a, b의 층에서 가장 오른쪽의 수를 저장하기 위해
    # 왜? 각 층에서 몇번째인지 알아내고자 해서 !
    end = 1
    next = 2
    floor = 1
    a_floor, b_floor = 1, 1
    a_max, b_max = 1, 1
    a_flag, b_flag = False, False

    while a_flag == False or b_flag == False:
        if a_flag == False and end >= a:
            a_floor = floor
            a_max = end
            a_flag = True
        if b_flag == False and end >= b:
            b_floor = floor
            b_max = end
            b_flag = True

        end += next
        next += 1
        floor += 1

    # 이동을 해야지
    # a, b 각 층에서의 idx 를 구하자
    a_idx = a_floor - (a_max - a)
    b_idx = b_floor - (b_max - b)

    if a > b:
        result = goFloor(a_idx, b_idx, a_floor, b_floor)
    else:
        result = goFloor(b_idx, a_idx, b_floor, a_floor)


    print("#{} {}".format(tc, result))

