# 1210. ladder

> 사다리타기를 통해 지정된 도착점에 갈 수 있는 시작점을 출력하는 문제



## 내 생각



`'시작점은 많지만 끝점은 하나다! 그러니 끝점부터 출발해서 시작점을 향해 가다보면 결과가 나올 것 이다.'` 라고 생각하여 문제를 풀이하였다.

이런문제를 보게되면 당연하게 bfs를 생각하게 돼서 바로 queue를 이용하려고 하는데 설계 안하고 바로 코드를 직접짜다가 뒤늦게야 깨달았다..

`사다리 타기는 옆으로 갈 수 있으면 무조건 옆으로 가고.. 그리고 동시에 좌 우로 갈 수 있는 가능성이 있지 않다..`

이걸 깨달으니 굳이 bfs를 쓸 필요가 없고 for문을 통해 다음 노드를 탐색하되 **왼쪽, 오른쪽을 먼저 탐색**하고 갈 수 있는 곳이라면 이동, break! 하면 된다는 것을 알게 되었다 ㅎㅎ

그래서 문제없이 풀이 완료 !!



## 코드

- 델타 리스트 선언, 메인 코드

```python
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
```

