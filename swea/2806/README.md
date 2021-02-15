# 2806. N-Queen

> N*N 의 체스판에 N개의 퀸을 두었을 때 서로 공격받지 않는 경우의 수를 출력



## 내 생각

일단 처음 문제를 보자마자 든 생각은 재귀적으로 풀면 괜찮을 것이라고 생각했다.

재귀 함수를 작성할 때 기저조건을 선정하는 것이 첫번째 할 일인데, 나는 **퀸은 당연히 같은 행에는 존재하면 안된다는 점**을 활용해서 함수를 작성했다.

1번째 행부터 N번째 행까지 재귀적으로 돌면서 N+1번째 행에 접근했을 때 결과를 1 더해주는 방식이다.

이렇게 하면 애초에 경우의 수가 없으면 N+1행에 접근할 수가 없다.

그럼 이제 퀸을 현재 행에서 둘 수 있는 조건을 작성해야 했다.

다음 행에는 퀸을 아직 두지 않았기 때문에 **밑을 검사할 필요는 없고, 위, 오른쪽 위 대각선, 왼쪽 위 대각선을 검사**해서 퀸이 존재하지 않다면 다음 행으로 넘어가게 함수를 작성하였다.

처음에는 답이 안나왔는데.. 찾아보니 재귀를 빠져나왔을 때 다시 배열을 업데이트 해주는 걸 또 깜빡했다.. ㅎ



## 코드

- 재귀적으로 퀸을 놓기

```python
def putQueen(current, n):
    if current == n: # 기저 조건 / 여기까지 왔다면 n개의 퀸을 다 배치한 거지 !
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
                    if not inRange(ny, nx, n): # 체스판 밖으로 가면 (다른 함수)
                        break
                    if board[ny][nx]:
                        flag = True
                        break
            
            if not flag:
                # 오른쪽 위 대각선
                for i in range(1, current+1):
                    ny = current - i
                    nx = j + i
                    if not inRange(ny, nx, n): # 체스판 밖으로 가면
                        break
                    if board[ny][nx]:
                        flag = True
                        break
            
            if not flag:
                board[current][j] = 1
                putQueen(current+1, n)
                board[current][j] = 0
```

