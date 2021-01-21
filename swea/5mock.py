dx = (1, 1, -1, -1, 1, 0, -1, 0)
dy = (1, -1, 1, -1, 0, 1, 0, -1)

def inRange(x, y, length):
    if x < 0 or x >= length or y < 0 or y >= length:
        return False
    else:
        return True

def getResult(count, row, col, dir, board, lenght):
    if count >= 5:
        return True
    else:
        ny = row + dir[0]
        nx = col + dir[1]
        if not inRange(ny, nx, lenght):
            return False
        if board[ny][nx] == '.':
            return False
        if board[ny][nx] == 'o':
            return getResult(count+1, ny, nx, dir, board, lenght)
def main():
    T = int(input())
    for t in range(1, T+1):
        flag = False
        length = int(input())
        input_list = []
        for row in range(length):
            col = input()
            input_list.append(col)
        for i, row in enumerate(input_list):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                else:
                    for d in range(8):
                        dir = [dy[d], dx[d]]
                        flag = getResult(1, i, j, dir, input_list, length)
                        if flag:
                            break
                if flag:
                    break
            if flag:
                break
        result = 'YES' if flag else 'NO'

        print(f'#{t} {result}')
        
if __name__ == "__main__":
    main()