import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    memory = input()

    one_flag = False
    result = 0
    for i in range(len(memory)):

        if one_flag == False and memory[i] == '1':
            result += 1
            one_flag = True
            continue

        if one_flag and memory[i] == '0':
            result += 1
            one_flag = False
            continue

    print('#{} {}'.format(tc, result))
