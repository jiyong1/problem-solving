# 2814. 최장 경로

> 그래프의 정점과 간선 정보를 제공하고 이를 통해 최장 경로를 얻어낸다.



## 내 생각



c++로 알고리즘 문제를 공부할 때 풀었다면 **vector 자료구조 활용해서 깊이 우선 탐색(dfs)** 사용하면 바로 풀 수 있을 난이도의 문제였다..

그런데 python으로 알고리즘 문제를 풀 고 있는 중이고.. vector 자료구조를 대신해서 사용하는 다양한 **pythonic 자료구조**를 활용해서 dfs를 돌려야했는데 뭐가 효율적이고 올바른지 배운적이 없다.. (곧 배우겠지만!)

정점의 정보가 랜덤한 순서로 주어질테고 이차원 배열(list)를 만든다고 해서 무턱대고 `list[랜덤 정점].append(연결된 정점 리스트)`를 하게 되면 index에러가 일어날 게 분명했다.. 그래서! **dictionary**를 사용했다..

그리고는 재귀 함수로 현재 위치에서 더 이상 갈 곳이 없을 때 (이미 다 방문한 정점만 존재) 결과 값과 비교하여 최대의 결과를 남겨 놓는 형식으로 함수를 작성했다.

또한 시작점을 하나로 잡으면 분명 문제가 일어날 것이기 때문에 모든 점을 시작으로 dfs를 전부 돌렸다!



## 코드

- dfs

```python
def dfs(current, cnt):
    global result
    flag = False

    # 더 이상 방문할 곳이 없는지 확인!
    for i in graph[current]:
        if not visited[i]:
            flag = True
            break

    # 방문할 곳이 없다면
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
```



- 그래프 생성

```python
graph = {}
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1] = graph.get(node1, []) + [node2]
    graph[node2] = graph.get(node2, []) + [node1]
```

