length = 0
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def inRange(x, y):
    if x < 0 or y < 0 or x >= length or y >= length:
        return False
    else:
        return True

def bfs(road):
    result = 0
    xlist = [0]
    ylist = [0]
    task_list = [0]
    tmp_list = [[0 for _ in range(length)] for _ in range(length)]
    while xlist:
        ct = task_list.pop(0)
        cx = xlist.pop(0)
        cy = ylist.pop(0)
        print(cx, cy)
        if cx == length -1 and cy == length - 1:
            if result == 0 or result > ct:
                result = ct
        else :
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]
                if not inRange(nx, ny):
                    continue
                if tmp_list[ny][nx] == 0 or tmp_list[ny][nx] > ct + int(road[ny][nx]):
                    tmp_list[ny][nx] = ct + int(road[ny][nx])
                    xlist.append(nx)
                    ylist.append(ny)
                    task_list.append(ct + int(road[ny][nx]))

    return result              

        

def main():
    global length
    T = int(input())
    for t in range(1, T+1):
        road = []
        length = int(input())
        for row in range(length):
            tmp = list(input())
            road.append(tmp)
        
        print(f'#{t} {bfs(road)}')


if __name__ == "__main__":
    main()