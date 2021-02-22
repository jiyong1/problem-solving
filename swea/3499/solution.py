import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    card = input().split()
    cri = N//2 if N%2 == 0 else N//2 + 1
    first = card[:cri]
    second = card[cri:]
    lst = []

    for i in range(len(second)):
        lst.append(first[i])
        lst.append(second[i])

    if len(lst) != N:
        lst.append(first[-1])

    result = ' '.join(lst)

    print('#{} {}'.format(tc, result))