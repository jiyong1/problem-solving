from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def inRange(x, y):
    if x < 0 or y < 0 or x >= length or y >= length:
        return False
    else:
        return True

def bfs():
    result = 0
    q = deque()
    q.append((0, 0))
    while q:
        cy, cx = q.popleft()
        ct = tmp_list[cy][cx]

        if cx == length -1 and cy == length - 1:
            if result == 0 or result > ct:
                result = ct
        else :
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]
                
                if not inRange(nx, ny):
                    continue
                if ny == 0 and nx == 0:
                    continue
                nt = ct + int(road[ny][nx])

                if tmp_list[ny][nx] == -1 or tmp_list[ny][nx] > nt:
                    tmp_list[ny][nx] = nt
                    q.append((ny, nx))

    return result              

        

T = int(input())
for t in range(1, T+1):
    length = int(input())
    road = [list(map(int, list(input()))) for _ in range(length)]
    tmp_list = [[-1]*length for _ in range(length)]
    tmp_list[0][0] = 0
    result = bfs()        
    print(f'#{t} {result}')