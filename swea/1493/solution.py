import sys
sys.stdin = open('input.txt')

def findXY(num):
    row = 1
    row_st = 1
    plus = 1
    while True:
        if row_st == num:
            return row, 1
        elif row_st > num:
            row = row-1
            row_st -= plus - 1
            break

        row += 1
        row_st += plus
        plus += 1


    current = row_st
    # print(current)
    col = 1
    while True:
        if current == num:
            return row, col

        current +=1
        row -= 1
        col += 1




def findNum(y, x):
    stRow = y+x-1
    row = 1
    num = 1
    plus = 1
    while row < stRow:
        row += 1
        num += plus
        plus += 1


    return num + x - 1

T = int(input())

for tc in range(1, T+1):
    p, q = map(int, input().split())
    py, px = findXY(p)
    qy, qx = findXY(q)
    print('#{} {}'.format(tc, findNum(py+qy, px+qx)))
