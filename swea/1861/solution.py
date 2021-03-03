import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def canIGo(cy, cx, num):

    for d in range(4):
        ny = cy + dy[d]
        nx = cx + dx[d]

        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue

        if arr[ny][nx] == num + 1:
            return 1
    else:
        return 0

def bfs(q):
    result_d = 0
    result_s = 0

    while q:
        cy, cx, clen = q.popleft()
        cnum = arr[cy][cx]

        if clen > result_d:
            result_d = clen
            result_s = cnum
        elif clen == result_d and result_s > cnum:
            result_s = cnum

        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue

            if arr[ny][nx] == cnum - 1:
                q.append([ny, nx, clen+1])
                break

    return result_s, result_d

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 끝 점은 무조건 있다. (방문할 수 있는 방의 수가 0, 나보다 1 큰게 없음)
    # 끝점들 에서 부터 bfs로 탐색하고 가장 많이 방문 할 수 있는 부분을 출력하면 될 거 같음
    # 만약에 모든 점에서 bfs나 dfs를 돌리면 답은 얻을 수 있지만 엄청 오래걸림

    q = deque()

    for i in range(N):
        for j in range(N):
            if canIGo(i, j, arr[i][j]):
                continue
            q.append([i, j, 1])



    # 끝 점들에서 bfs 탐색
    s, d = bfs(q)

    print('#{} {} {}'.format(tc, s, d))
