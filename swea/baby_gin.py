import sys
sys.stdin = open("input.txt")

T = int(input())

def getResult(lst):
    count = [0]*10
    card_count = 0
    for num in lst:
        count[num] += 1
        card_count += 1
        if count[num] == 3:
            count[num] = 0
            card_count -= 3
    if card_count == 0:
        return 1

    i = -1
    while i < 7:
        i += 1
        if count[i] == 0: continue
        if count[i+1] != 0 and count[i+2] != 0:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            card_count -= 3
            i -= 1

        if card_count == 0:
            break


    if card_count == 0:
        return 1
    else:
        return 0


for tc in range(1, T+1):
    lst = list(map(int, input()))
    result = getResult(lst)
    print("#{} {}".format(tc, result))

