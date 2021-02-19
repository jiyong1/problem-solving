# 1929. 소수 구하기

> 1 <= M < N <= 1000000 일 때 M과 N 사이의 소수를 출력한다.



## 내 생각

에라토스테네스의 체를 많이 들어봤다..

근데 이해를 해야 내꺼지.. 일단 소수의 배수들은 소수가 아님을 저장한다는게 알고리즘의 내용이다.

왜 **소수**의 배수이냐 하면 어차피 2부터 시작해서 소수의 배수들을 소수가 아니라고 지정하게 되면 소수가 아닌 애들의 배수는 소수의 배수들로 검증이 완료 됐을 것이다.

그렇다면 왜? N의 제곱근 만큼만 하면 되냐 !!

만약 N이 120이라고 했을 때! 120의 제곱근보다 큰 정수 중 가장 작은 11까지 한다고 가정해보자.

11 * 10 까지 진행 될 것이고, 이 후 120보다 작은 소수의 배수는 어떻게 처리할 것이가 고민할 수 있다.

13으로 가볼까? 그래봤자 13*9 까지 할 것인데.. **이때 주목할 점은 13이 아니라 9다!**

그럼 **9는 3의 배수이고 이는 이전에 3의 배수들을 처리할 때 3*39**가 소수가 아님을 처리했을 것!!!

그렇다.. **주목할 점은 앞의 수가 커지면 뒤 수는 작아질 거고..** 뒤 수에 주목하면 이미 처리했다는 점을 알 수 있다!



## 코드

- 에라토스테네스의 체를 이용한 소수 구하기

```python
M, N = map(int, input().split())

# M과 N 사이는 고작 백만이네.. 소수 임을 저장할 배열을 만들자..
isPrime = [True] * (N+1)
isPrime[1] = False

# 소수의 배수를 찾아 소수가 아님을 저장한다..
# 에라토스테네스의 체
for i in range(2, int(N**0.5)+2):
    if not isPrime[i]:
        continue
    current = 2
    while i*current <= N:
        isPrime[i*current] = False
        current += 1

for i in range(M, N+1):
    if isPrime[i]:
        print(i)
```
