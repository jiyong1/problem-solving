import sys
sys.stdin = open('input.txt')

def dfs(idx, left_sum, right_sum, bit):
    if right_sum > left_sum:
        return 0
    if equal_lsum_visit[bit][left_sum]:
        return equal_lsum_visit[bit][left_sum]
    if idx == N:
        equal_lsum_visit[bit][left_sum] = 1
        return 1
    else:
        case = 0
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            case += dfs(idx+1, left_sum+weights[i], right_sum, bit|(1<<i))
            case += dfs(idx+1, left_sum, right_sum+weights[i], bit|(1<<i))
            visited[i] = False
        
        equal_lsum_visit[bit][left_sum] = case
        return case
        


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    lsum = sum(weights)
    visited = [False for _ in range(N)]
    equal_lsum_visit = [[0 for _ in range(lsum+1)] for _ in range(1<<N)]
    result = dfs(0, 0, 0, 0)

    print('#{} {}'.format(tc, result))