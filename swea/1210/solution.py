import sys
sys.stdin = open("input.txt")

def inRange(x, y):
    if x >= 100 or y >= 100 or x < 0 or y < 0:
        return False
    else:
        return True

T = 10

dy = [0, 0, -1]
dx = [-1, 1, 0]


for tc in range(1, T+1):
    # tst : 테스트 케이스 번호
    # board : 사다리 2차원 배열
    # 방문 여부 -> 역으로 돌아가는 것을 방지 !
    tst = int(input())
    N = 100
    board = [input().split() for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = 0

    cy, cx = 99, 0

    # 도착점을 찾자
    # 시작점은 많지만 도착점은 하나니깐 도착점에서 시작해야 효율적이지
    for i in range(N):
        if board[99][i] == '2':
            cx = i

    while True:
        # 발도장 찍고..
        visited[cy][cx] = True

        # 도착!
        if cy == 0:
            result = cx
            break

        # 좌, 우 먼저 탐색하고 없으면 위로 올라가자..
        for d in range(3):
            ny = cy + dy[d]
            nx = cx + dx[d]

            if inRange(ny, nx) == False or board[ny][nx] == '0' or visited[ny][nx]:
                continue

            cy = ny
            cx = nx
            break

    print("#{} {}".format(tc, result))

