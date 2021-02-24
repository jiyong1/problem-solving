# 1868. 파핑파핑 지뢰찾기

> 지뢰찾기를 완수하기 위해 클릭해야하는 횟수의 최솟값을 출력하라.



## 내 생각

그냥 별 생각 없이 푼 문제다.. 뭐 좀 더 효율적으로 풀 수 있는 방법에 대해 생각해보고 시도를 몇번 해봤지만 다 문제가 될 풀이법이어서 생략하고 넘어가겠다..

일단 비어있는 칸 즉, 지뢰가 아닌 칸의 8방향을 탐색해서 해당 칸에 어떤 숫자가 들어가야하는지 확인했다.

숫자를 확인하면서 0이 들어가야하는 공간의 y좌표와 x좌표를 리스트에 담아놨다.

**`최소로 클릭하기 위해서는 우선적으로 0을 클릭해서 클릭을 최소화`** 해야한다. 따라서 이미 클릭되지 않은 0을 클릭(클릭 +1)하게 하여 주변을 전부 클릭(visited를 뒤집는다/ 0주변의 0또한 뒤집어줘야 한다.)하게 하였다.

그 후, 클릭되지않은 숫자들을 다시 클릭(클릭 + 1)해서 총 클릭횟수를 결과로 출력하였다.



## 코드

- 전체 코드

```python
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

```

