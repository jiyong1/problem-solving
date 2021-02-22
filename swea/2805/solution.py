import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

def getValue(fq, cq):
    result = 0
    while farm_q:
        cy, cx = fq.popleft()
        result += farm[cy][cx]

        cc = cq.popleft()

        if not cc:
            continue
        else:
            for d in range(4):
                ny = cy + dy[d]
                nx = cx + dx[d]
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                cq.append(cc-1)
                fq.append((ny, nx))

    return result


for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    go_count = (N-1)//2

    count_q = deque()
    farm_q = deque()
    count_q.append(go_count)
    farm_q.append((N//2, N//2))
    visited[N//2][N//2] = True

    result = getValue(farm_q, count_q)

    print('#{} {}'.format(tc, result))