from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def team(c):
    if c == "W":
        return 0
    else:
        return 1

def bfs(i, j, who):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    count = 0

    while q:
        cy, cx = q.popleft()
        count += 1

        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= M or visited[ny][nx]:
                continue
            
            if arr[ny][nx] != who:
                continue

            visited[ny][nx] = True
            q.append([ny, nx])

    return count**2

M, N = map(int, input().split())
visited = [[False for _ in range(M)] for _ in range(N)]

arr = [list(map(team, input())) for _ in range(N)]

result_list = [0, 0]

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        result_list[arr[i][j]] += bfs(i, j, arr[i][j])

print(*result_list)
