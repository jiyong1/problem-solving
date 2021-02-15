# 일단 당연히 같은 행에 있으면 안됨
# 그러니까 재귀적으로 돌면서 행에 하나씩 넣고 검사를 하는 방식으로 풀이하자
# 이전 행에는 퀸이 존재할 것이고 다음 행에는 존재하지 않을 것이야..
# 그러니까 위로 대각선 두개의 위로 세개를 검색해서 퀸이 존재하면 continue
def inRange(y, x, n):
    if y >= n or y < 0 or x >= n or x < 0:
        return False
    else:
        return True

def putQueen(current, n):
    if current == n: # 기저 조건
        global result
        result += 1
    
    else :
        for j in range(n): # current 행 / j 열
            # 이전의 퀸과 겹치나 확인하기 위한 flag
            flag = False
            
            # 위로 탐색
            for i in range(1, current+1):
                if board[current-i][j]:
                    flag = True
                    break
            
            if not flag:
                # 왼쪽 위 대각선
                for i in range(1, current+1):
                    ny = current - i
                    nx = j - i
                    if not inRange(ny, nx, n):
                        break
                    if board[ny][nx]:
                        flag = True
                        break
            
            if not flag:
                # 오른쪽 위 대각선
                for i in range(1, current+1):
                    ny = current - i
                    nx = j + i
                    if not inRange(ny, nx, n):
                        break
                    if board[ny][nx]:
                        flag = True
                        break
            
            if not flag:
                board[current][j] = 1
                putQueen(current+1, n)
                board[current][j] = 0


T = int(input())

for tc in range(1, T+1):
    # N : N*N 배열과 N개의 퀸
    N = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    putQueen(0, N)

    print('#{} {}'.format(tc, result))

