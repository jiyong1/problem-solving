import sys
sys.stdin = open("input.txt")

T = 11


for tc in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    # print(buildings)
    # 1. 두 방향으로 2만큼 거리까지 탐색을 해야한다.
    for idx in range(n):
        if not buildings[idx]:
            continue
        # 2. 한쪽이라도 조망권 확보가 어렵다면 flag 뒤집고 for문 continue
        flag = False

        # 3. 왼쪽 최소, 오른쪽 최소를 구하고 두개를 비교해서 둘 중 최소를 결과에 더한다!
        min = buildings[idx]

        # 3. 왼쪽 오른쪽 검사하자
        for i in range(1, 3):
            if buildings[idx-i] >= buildings[idx] or buildings[idx+i] >= buildings[idx]:
                flag = True
                break
            left = buildings[idx] - buildings[idx-i]
            right = buildings[idx] - buildings[idx+i]

            if left < right:
                current_min = left
            else:
                current_min = right

            if min > current_min:
                min = current_min

        if flag:
            continue

        result += min

    print("#{} {}".format(tc, result))

