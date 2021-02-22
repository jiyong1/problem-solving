import sys
sys.stdin = open("input.txt")

T = int(input())

def makeTable(current):
    global num
    num -= 1
    parents = num
    arr[current].append(parents)

    for i in range(len(my_son[current])):
        makeTable(my_son[current][i])

    arr[current].append(num)


for tc in range(1, T+1):

    # V : 정점의 총 수, E : 간선의 총 수, 공통 조상을 찾는 두 개의 정점 번호
    V, E, node1, node2 = map(int, input().split())

    # 간선 정보 1번째 -> 2번째
    # 가장 큰 번호+1 크기로 리스트를 만들자
    tree_info = list(map(int, input().split()))
    N = max(tree_info)
    my_mom = [0 for _ in range(N+1)]
    my_son = [[] for _ in range(N+1)]
    arr = [[] for _ in range(N+1)]
    num = 10001

    for i in range(0, len(tree_info), 2):
        parent = tree_info[i]
        child = tree_info[i+1]
        my_mom[child] = parent
        my_son[parent].append(child)

    makeTable(1)

    current = my_mom[node1]
    result = 0

    while True:
        if arr[current][0] >= arr[node2][0] and arr[current][1] <= arr[node2][1]:
            result = current
            break
        current = my_mom[current]

    num_sub = arr[result][0] - arr[result][1] + 1

    print("#{} {} {}".format(tc, result, num_sub))