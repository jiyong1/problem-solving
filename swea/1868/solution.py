import sys
sys.stdin = open('input.txt')


T = int(input())

# 8방향
dy = [0, 1, 0, -1, 1, -1, 1, -1]
dx = [1, 0, -1, 0, 1, -1, -1, 1]

def searchBomb(row, col):
    result = 0

    for d in range(8):
        ny = row + dy[d]
        nx = col + dx[d]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue

        if bomb[ny][nx] == '*':
            result += 1

    return result

def clickZero(row, col):
    visited[row][col] = True
    if bomb[row][col] != 0:
        return
    else:
        for d in range(8):
            ny = row + dy[d]
            nx = col + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or visited[ny][nx]:
                continue

            clickZero(ny, nx)


for tc in range(1, T+1):
    # 배열의 크기 N
    N = int(input())

    bomb = [list(input()) for _ in range(N)]

    # 8방향 탐색 -> 0 나오면 주위 또 탐색하자
    # 0 -> 탐색
    visited = [[False for _ in range(N)] for _ in range(N)]
    zeros = []
    result = 0
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '.':
                x = searchBomb(i, j)
                if x == 0:
                    zeros.append([i, j])
                bomb[i][j] = x

    # 0번 클릭 하자
    for zn in zeros:
        if visited[zn[0]][zn[1]]:
            continue
        else:
            clickZero(zn[0], zn[1])
            result += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and bomb[i][j] != '*':
                result += 1



    print('#{} {}'.format(tc, result))
