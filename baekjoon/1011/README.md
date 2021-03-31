# 1011. Fly me to the Alpha Centauri

## 생각..
일단 처음에 어디서 시작돼서 끝이나든 길이에 따라서 답이 결정난다는 것을 알게되었다. 그리고 테스트 케이스 형식의 문제이니까 **데이터를 쌓아가면서 존재하지 않는 상황일 때는 데이터를 더 쌓고, 존재하는 상황이라면 이분탐색으로 빠르게 정답을 가져오면 되겠다고 생각했다..**

근데 역시 문제는 **어떻게 마땅한 데이터를 찾을것인가..** 그냥 무작정 손으로 여러 상황을 다 적어보다가 규칙 하나를 겨우 알아내게 됐다. (앞에서 언급한바와 같이 시작 끝 점의 숫자는 의미가 없고 시작과 끝 사이의 거리가 중요하니 0부터 시작한다고 가정한다.)
```
1 -> 1 /1번 이동
121 -> 4 /3번 이동
12321 -> 9 /5번 이동
1234321 -> 16 /7번 이동
123454321 - > 25 /9번 이동
```

이렇게 적으면 이게 무슨 규칙이지 라고 생각할 수 있는데 놀랍게도.. 적어보면서 규칙을 찾아보면

1, 2번이동 1개씩
3, 4번이동 2개씩
5, 6번이동 3개씩
...

이런 규칙을 얻어낼 수 있다!!!
그니깐 이 규칙을 통해 데이터를 쌓고 지금 얻고자 하는 길이의 데이터가 존재한다면 그냥 이분탐색을 하면 되는 것이다.

## 코드

```python
def binarySearch(length):
    st = 0
    end = len(arr)-1

    if arr[st][0] == length:
        return arr[st][1]
    elif arr[end][0] == length:
        return arr[end][1]
    else:
        while end - st > 1:
            mid = (st+end)//2
            if arr[mid][0] >= length:
                end = mid
            else:
                st = mid

        return arr[end][1]


T = int(input())
# 2번씩 더한다. -> 1, 1, 2, 2, 3, 3
num_count = 0
num = 0
plus = 1
count = 1
arr = []

for tc in range(1, T+1):
    st, end = map(int, input().split())
    length = end - st

    # 데이터를 더 쌓자
    if num < length:
        while num < length:
            num += plus
            num_count += 1
            if num_count == 2:
                plus += 1
                num_count = 0

            arr.append((num, count))
            count += 1
        
        print(arr[-1][1])
    else:
        print(binarySearch(length))
```
