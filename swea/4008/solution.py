import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(current, _pre):
    if current == N:
        global my_min, my_max
        if my_min > _pre:
            my_min = _pre
        if my_max < _pre:
            my_max = _pre
        return
    else:
        for o in range(4):
            if not operator[o]:
                continue
            if o == 0:
                now = _pre + nums[current]
            elif o == 1:
                now = _pre - nums[current]
            elif o == 2:
                now = _pre * nums[current]
            else:
                if nums[current] == 0:
                    continue
                now = int(_pre / nums[current])

            operator[o] -= 1
            dfs(current+1, now)
            operator[o] += 1

for tc in range(1, T+1):
    N = int(input())

    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    my_min = 100000000
    my_max = -100000000

    dfs(1, nums[0])

    print('#{} {}'.format(tc, my_max-my_min))