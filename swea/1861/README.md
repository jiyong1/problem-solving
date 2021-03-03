# 1861. 정사각형 방

> 상하좌우로 조건을 만족하는 경우 방을 이동할 수 있을 때, 가장 많이 이동할 수 있는 시작점과 그 길이를 출력한다.



## 내 생각

문제를 딱 보자마자 **그냥 모든 점에서 dfs나 bfs를 통해 탐색을 하게 되면 엄청난 시간이 걸릴 것이라고 판단이 되었다**.

그래서 나는 좀 다른 방식으로 풀이를 진행하였다.

문제의 2차원 배열에서 **모든 원소의 숫자가 다르기 때문에** **`각 점에서 이동할 수 있는 방은 한개 이하`**일 것이고, 갈 수 있는 방이 더 이상 존재하지 않는 방을 큐에 넣어두고 그 방에서 **반대로 거슬러 올라가면서 탐색**을 하게되면 **`N*N배열에서 시간복잡도가 O(N^2)`**이 나올 것이기 때문에 충분히 풀이가 가능할 것이라고 생각했다!



## 코드

1. 더 이상 갈 수 있는 방이 존재하지 않는 방을 탐색 
   - 큐에 `[y좌표, x좌표, 1(depth)]` 를 넣어준다.
2. bfs를 통해 큐가 빌 때까지 탐색한다.
   - 거슬러 올라가는 조건을 만족한다면 다음 좌표와 현재 depth+1을 큐에 넣어준다.
   - 최대 깊이를 계속해서 업데이트
   - 최대 깊이와 현재 깊이가 같다면 시작 점을 더 낮은 수로 지정



```python
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

```

