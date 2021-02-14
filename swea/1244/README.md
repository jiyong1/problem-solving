# 1244 최대 상금

> 주어진 카드의 순서를 정해진 횟수 만큼 바꾸어 최대의 숫자를 만드는 문제



## 내 생각



처음에는 greedy하게 접근하여 첫 index부터 마지막까지 돌면서 나중에 바꿀 index까지 신경쓰며 가장 적합한 숫자를 찾아 바꾸는 형식으로 생각했다..

예시를 말하면 **32888** 의 숫자 카드가 있을 때

가장 큰 숫자와 나보다 작은 숫자를 찾고, 나중에 카드를 바꿀 기회가 존재한다면 **맨뒤의 8과 바꾸는 것이 아니라 2를 위해 두번째 8과 위치를 교환한다..** 라는 생각..

근데 과연 이게 D3의 문제 난이도에서 생각해야하는 구조인가라는 의문이들었다..

그래서 결과적으로 **모든 상황**을 고려하되! 나보다 뒤에 있는 것 중에서 **나보다 큰놈이랑은 무조건 교환**하는 **재귀 함수**를 구현하였다 !

이 때 교환 횟수가 지정된 교환 횟수보다 적다 하더라도 **내림차순으로 정렬된 배열과 동일**하다면.. 재귀를 **전부 빠져나와 다른 로직을 통해 결과**를 얻어내는 코드를 작성하였다.



## 코드



- 재귀 함수

```python
def getResult(st, cnt):
    global result
    global flag
    global remain, count
    # 이미 정렬이 돼버렸다..!
    if numbers == numbers_max:
        flag = True
        remain = count - cnt
        return
    # 바꿀 수 있는 기회를 다 사용하였다.
    if cnt == count:
        current = int(''.join(map(str, numbers)))
        if current > result:
            result = current
        return
    else:
        for i in range(st, len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    getResult(i+1, cnt+1)
                    # 재귀 다빠져나와버려
                    if flag:
                        return
                    numbers[i], numbers[j] = numbers[j], numbers[i]
```



- 정렬이 완료됐고, 카드를 교환해야하는 횟수가 남아있을 때

```python
if flag:
    # 남은 횟수가 짝수면 수 두개를 계속 반복해도 결과는 같다.
    if not remain%2:
        result = int(''.join(map(str, numbers)))
    # 홀수 일때
    else:
        # 같은 수가 여러개 존재한다면, 그 두개를 바꿔주면 되니.. 결과는 동일하다
        same_flag = False
        
        # 정렬된 배열일 때 전과 후 비교만 해줘도 동일한 값이 여러개 존재하는지 확인할 수 있지!
        for i in range(1, len(numbers)):
            if numbers[i-1] == numbers[i]:
                same_flag = True
                break
        if same_flag:
            result = int(''.join(map(str, numbers)))
           
        # 같은 수가 존재하지 않고.. 남은 횟수가 홀수라면 맨뒤의 두개를 바꿔주는게 가장 높은 수다!
        else:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
            result = int(''.join(map(str, numbers)))
```

