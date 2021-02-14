import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(current, cnt):
    global result
    flag = False
    for i in graph[current]:
        if not visited[i]:
            flag = True
            break

    if not flag:
        if cnt > result:
            result = cnt

    else:
        for i in graph[current]:
            if visited[i]:
                continue
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False


for tc in range(1, T+1):
    # dict 를 만들어서 각 정점에 연결된 정점의 정보를 저장해보자
    # N 정점의 개수, M 간선의 개수
    N, M = map(int, input().split())
    graph = {}
    result = 1
    visited = [False]*(N+1)

    for _ in range(M):
        node1, node2 = map(int, input().split())
        graph[node1] = graph.get(node1, []) + [node2]
        graph[node2] = graph.get(node2, []) + [node1]

    for key in graph.keys():
        visited[key] = True
        dfs(key, 1)
        visited[key] = False

    print("#{} {}".format(tc, result))

