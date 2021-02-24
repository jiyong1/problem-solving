# 17298. 오큰수

> 순열의 각 인덱스에서 오른쪽에 존재한 큰 수중 가장 왼쪽에 존재하는 큰 수를 담아 출력한다.



## 내 생각

전에 프로그래머스를 통해서 탑이라는 문제를 풀었었는데 풀이 방법이 거의 유사했다.

풀이 방법은 일단 stack 자료구조를 만들어서 현재 순열의 숫자 보다 큰 자료가 존재할 때 까지 stack을 pop하는 방법이다. stack이 비어있다는 것은 내 오른쪽에 나보다 큰 수가 없다는 것이므로 -1을 담는다.

왜 이렇게 풀어도 되냐 하면.. **`각 인덱스의 입장에서 나보다 큰 놈이 없다는 것은 그 다음으로 탐색하는 왼쪽의 입장에서도 나 빼고는 볼 필요가 없다는 것`**이다. 내 왼쪽은 내가 크면 곧 내가 오큰수이니까.. 그러니까 스택을 담기 위해 뒤에서부터 앞으로 탐색을 해야한다 !

그리고 문제를 풀면서 한가지 깨달은 점은.. 결과를 담는 자료형을 string으로하면 오래 걸린다는 것을 깨달았다.. 문제 풀이는 똑같은데 리스트에 담고 최종적으로 string으로 변환하는것은 pass가 떴는데.. string의 더하기 연산을 하니 fail이 떴다..!



## 코드

- 전체 코드

```python
# 각 순열에서 오른쪽만 바라본다.
# 맨 오른쪽 부터 탐색을 시작한다.
# 스택에 나보다 큰게 보일 때까지 스택을 비운다
# 왜 가능한가? 어차피 내가 제일 큰놈이라면 내 바로 왼쪽에서도 나를 볼거야

# N = 수열의 길이

N = int(input())

permutation = list(map(int, input().split()))

# 오른쪽에 나보다 큰 놈을 확인하기 위해서
right_stack = []

# 맨 마지막은 -1
result = [-1]

right_stack.append(permutation[-1])

# 뒤에서 두번째부터 0 까지
for i in range(len(permutation)-2, -1, -1):
    current = permutation[i]
    now = -1

    while right_stack and right_stack[-1] <= current:
        right_stack.pop()

    if right_stack:
        now = right_stack[-1]

    right_stack.append(current)

    result.append(now)


print(' '.join(map(str, result[::-1])))
```



