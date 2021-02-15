
def Pseudorandom_func(p, q, m, pre):
    return (p*pre + q) % m

T = int(input())

for tc in range(1, T+1):
    s, p, q, m = map(int, input().split())
    arr = [0]*m
    arr[s] = 1
    count = 1
    result = 0

    while True:
        count += 1
        next = Pseudorandom_func(p, q, m, s)
        if arr[next]:
            result = count - arr[next]
            break

        s = next
        arr[s] = count

    print("#{} {}".format(tc, result))