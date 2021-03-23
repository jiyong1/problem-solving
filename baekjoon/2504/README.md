# 2504 괄호의 값

> 올바른 괄호 형태일 때 괄호의 값을 출력하시오.

## 풀이 과정

처음에 풀이 과정을 생각했을 때는 괄호의 깊이 맞는 배열에 수를 넣은 후 최종적으로 다 곱해줘야하나 생각했다.
그런데 생각해보니 결국 괄호의 깊이가 무한정 깊다고 해도 `()`형태나 `[]`형태 같이 괄호안에 아무것도 존재하지 않는 형태가 무조건 있다는 점을 생각해냈다..!
그럼 괄호안에 괄호, 괄호안에 괄호.. 이렇게 들어가다가 **처음으로 괄호안에 아무것도 들어있지 않은 경우 현재까지 깊이까지 곱한 값을 결과에 더해주면 되겠구나!** 라고 생각했다.
이렇게 풀려면 유효한 닫힌 괄호일 때 두 가지 조건으로 풀이해야한다.

- 유효한 닫힌 괄호를 만났을 경우

1. `괄호안에 자식 괄호가 존재할 경우`
   - 주어진 조건에 맞추어 2나 3으로 현재 까지 곱한 값을 나누어준다.`(:2, [:3`
2. `괄호안에 아무것도 존재하지 않는 경우`
   - 현재까지 곱한 값을 결과 값에 더해준다



## 코드

```python
dic = {')': '(', ']': '['}
c2num = {'(': 2, '[': 3}
stack = []

user_str = input()
current = 1
result = 0

for idx, c in enumerate(user_str):
    if c in c2num.keys():
        stack.append(c)
        current *= c2num[c]
    else:
        if not stack:
            result = 0
            break
        pre = stack.pop()

        if pre != dic[c]:
            result = 0
            break

        if user_str[idx-1] == pre:
            result += current
        
        current //= c2num[pre]

if stack:
    result = 0
    
print(result)
```

