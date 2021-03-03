import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10

def bfs(q):
    result = 0
    latest = 0

    while q:
        cstudent, clength = q.popleft()

        if clength > latest:
            result = cstudent
            latest = clength
        elif clength == latest and result < cstudent:
            result = cstudent

        for i in range(len(phone_book[cstudent])):
            next = phone_book[cstudent][i]

            if visited[next]:
                continue

            visited[next] = True

            q.append([next, clength+1])

    return result

for tc in range(1, T+1):
    N, start = map(int, input().split())
    link_list = list(map(int, input().split()))
    last_num = max(link_list)

    # 그래프 구현
    phone_book = [[] for _ in range(last_num+1)]

    for i in range(0, N, 2):
        phone_book[link_list[i]].append(link_list[i+1])

    # bfs의 시작점 큐에 넣고 발도장 찍기
    visited = [False for _ in range(last_num+1)]
    visited[start] = True

    q = deque()
    q.append([start, 0])

    result = bfs(q)


    print('#{} {}'.format(tc, result))