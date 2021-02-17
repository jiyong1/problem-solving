# 1493. 수의 새로운 연산

> 대각선으로 2차원 배열의 숫자가 증가하는 배열에서 주어진 문제를 풀이한다.



## 내 생각

일단 처음에는 매우 큰 착각을 가지고 문제 풀이를 시작했다.

p, q의 제한조건이 10000아래 이길래.. 100x100배열에서 대각선으로 배열의 수를 결정하는 줄 알고 먼저 100x100 배열을 생성했다.. 근데 이게 문제였다

사실 문제는 배열 크기의 제한없이 피라미드 처럼 대각선이 쭉 뻗어 나가는 형식이었다..(사각형이 아니라 삼각형이라고 보면 되는..)

그래서 문제를 처음부터 다시 풀이하였다.

일단 두가지 함수를 선언하였다. 첫 번째는 수를 매개변수로 받으면 해당 수가 존재하는 row, column을 return하는 함수, 두 번째는 row, col을 넘기면 해당 좌표에 존재하는 숫자를 return하는 함수였다. 



## 코드

- 수가 존재하는 row, column을 return하는 함수

```python
def findXY(num):
    row = 1
    row_st = 1
    plus = 1
    while True:
        if row_st == num:
            return row, 1
        elif row_st > num:
            row = row-1
            row_st -= plus - 1
            break

        row += 1
        row_st += plus
        plus += 1


    current = row_st
    # print(current)
    col = 1
    while True:
        if current == num:
            return row, col

        current +=1
        row -= 1
        col += 1
```



- row, col을 넘기면 해당 좌표에 존재하는 숫자를 return하는 함수

```python
def findNum(y, x):
    stRow = y+x-1
    row = 1
    num = 1
    plus = 1
    while row < stRow:
        row += 1
        num += plus
        plus += 1
```

