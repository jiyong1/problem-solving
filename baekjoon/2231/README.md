# 2231. 분해합

> 분해합과 생성자의 개념을 보고 주어진 수의 생성자 중 가장 작은 수를 출력한다.



## 내 생각

문제를 보고 생성자는 주어진 수 보다 절대 클 수 없기 때문에 `재귀를 이용`해서 풀이하면 풀 수 있을거라고 판단했다.

그래서 각각의 재귀에서 `0~9 순으로 각 자리에 수를 집어 넣으면서 그 수의 분해합을 자리수에 맞게 10의 길이 승으로 더해주면서 다음 단계의 재귀로 가는 형태`의 함수를 작성하였다. 이렇게 풀이하면 주어진 수가 100이상일때 생성자가 2자리 수여도 답을 얻어낼 수 있고, `0~9 순으로 하면서 최초로 생성자를 찾았을 때는 분명 그 수가 가장 작은 수`이기 때문에 적절한 답을 얻을 수 있을 것이라 생각했다.

두번의 제출에서 fail이 떴는데 처음에는 생성자가 존재하지 않을때 0을 대신해서 출력하는 것을 빼먹었고, 두 번째때는 18의 생성자가 9일 때 09로 출력하게 하여서 틀리게 되었다. 이 점은 string을 int로 바꾸면서 자동적으로 앞 0이 없어지게 처리하였다.



## 코드

- 생성자를 얻기 위한 재귀함수

```python
def getResult(current_sum, length, now_str):
    global flag
    if length < 0:
        global result
        if current_sum == N:
            result = now_str
            flag = True
            return

    else:
        for i in range(10):
            getResult(current_sum+i+(i*10**length), length-1, now_str+str(i))
            if flag:
                return



N = int(input())
result = ''
flag = False
getResult(0, len(str(N))-1, '')
if not result:
    result = 0
print(int(result))
```

