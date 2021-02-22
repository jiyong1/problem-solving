import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    card = input()
    card_list = [[0 for _ in range(14)] for _ in range(4)]
    shape_list = [13 for _ in range(4)]
    result = 0
    # S = 0
    # D = 1
    # H = 2
    # C = 3
    flag = False
    for i in range(0, len(card), 3):
        shape = -1
        if card[i] == 'S':
            shape = 0
        elif card[i] == 'D':
            shape = 1
        elif card[i] == 'H':
            shape = 2
        elif card[i] == 'C':
            shape = 3

        num = int(card[i+1:i+3])
        if card_list[shape][num]:
            result = 'ERROR'
            flag = True
            break

        card_list[shape][num] += 1
        shape_list[shape] -= 1

    
    if not flag:
        result = ' '.join(map(str, shape_list))

    print('#{} {}'.format(tc, result))