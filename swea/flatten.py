import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    flatten_count = int(input())
    boxes = list(map(int, input().split()))
    count = [0]*101

    # 하나하나 쌓아주면서 각 인덱스 몇번인지 확인하고 또 최저값 확인하고 하면 약간 비효율적이니..
    # 1. 최고와 최저 높이를 저장하자
    min = 101
    max = 0
    for box in boxes:
        count[box] += 1
        if box < min :
            min = box
        if box > max :
            max = box

    # dupped 시작하자
    for _ in range(flatten_count):
        # 평탄화를 시키면 max와 min의 count가 하나씩 줄고 max-1 min+1의 카운트가 증가 하겠지.
        count[max] -= 1 # 98 max 4 -> 3 -> 2
        count[max-1] += 1  # 97 + 1 +1 # 3 -> 4
        count[min] -= 1
        count[min+1] += 1
        # 더 이상 min 박스의 수가 없다면 min을 바꾼다
        while count[min] == 0: # not Flase -> True '' [] () 0이냐 아니냐?
            min += 1
        # 더 이상 max 박스의 수가 없다면 max를 바꾼다
        while not count[max]: # count 99 -> 0 98
            max -= 1

    result = max - min

    
    print("#{} {}".format(tc, result))

