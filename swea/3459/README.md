# 3459. 승자 예측하기

> 1 ~ N 까지 숫자가 주어질 때 1부터 2x, 2x+1을 하여 최초로 N을 초과하는 사람이 지는 게임



## 내 생각

내가 제일 싫어하는 유형의 문제였다..

아이패드를 키고 이럴 때는..? 저럴 때는..? 하면서 생각하다보니 자꾸 앞으로 가질 못하고 뒤에서 머물고 있는 나의 모습을 볼 수 있었다..

그냥 계속 끄적이다 보니 `1 / 4 / 4 / 16 / 16 ...` 의 규칙을 얻어내서 문제를 풀긴 했지만 아직까지도 너무 헷갈린다..

뭐 풀이의 이유를 설명하기 보다는 생각을 했던 방법에 대해 언급해보자면

뒤에 숫자는 **`절. 때.`** 생각하지 않고 만약 이 숫자가 나온다면..?으로 생각하며 그 범위를 넓혀갔다..

그러다 보니 위에 언급한 패턴으로 승자가 변한다는 것을 파악했다.

참.. 최선을 다한다는 말이 제일 애매한 말인 것 같다 ㅋㅋㅋ..



## 코드

```python
import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    # 0 : alice / 1 : bob
    result = 1

    start = 1
    mul = 1
    both = False

    while N > start:
        result = 1 if result == 0 else 0

        if not both:
            both = True
            mul *= 4
        else:
            both = False


        start += mul


    if result == 0:
        result = 'Alice'
    else:
        result = 'Bob'

    print("#{} {}".format(tc, result))
```



