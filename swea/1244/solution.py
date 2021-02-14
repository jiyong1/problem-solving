import sys
sys.stdin = open("input.txt")

T = int(input())

def getResult(st, cnt):
    global result
    global flag
    global remain, count
    if numbers == numbers_max:
        flag = True
        remain = count - cnt
        return
    if cnt == count:
        current = int(''.join(map(str, numbers)))
        if current > result:
            result = current
        return
    else:
        for i in range(st, len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    getResult(i+1, cnt+1)
                    if flag:
                        return
                    numbers[i], numbers[j] = numbers[j], numbers[i]


for tc in range(1, T+1):
    #숫자 카드와 교환 횟수를 저장한다.
    numbers, count = input().split()
    count = int(count)
    numbers = list(map(int, numbers))
    numbers_max = sorted(numbers, reverse=True)
    remain = 0
    result = 0
    flag = False
    getResult(0, 0)

    # 이미 numbers가 numbers_max
    if flag:
        if not remain%2:
            result = int(''.join(map(str, numbers)))
        else:
            same_flag = False
            for i in range(1, len(numbers)):
                if numbers[i-1] == numbers[i]:
                    same_flag = True
                    break
            if same_flag:
                result = int(''.join(map(str, numbers)))
            else:
                numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
                result = int(''.join(map(str, numbers)))

    print("#{} {}".format(tc, result))

