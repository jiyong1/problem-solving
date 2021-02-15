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
