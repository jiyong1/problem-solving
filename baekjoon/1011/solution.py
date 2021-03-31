def binarySearch(length):
    st = 0
    end = len(arr)-1

    if arr[st][0] == length:
        return arr[st][1]
    elif arr[end][0] == length:
        return arr[end][1]
    else:
        while end - st > 1:
            mid = (st+end)//2
            if arr[mid][0] >= length:
                end = mid
            else:
                st = mid

        return arr[end][1]


T = int(input())
# 2번씩 더한다. -> 1, 1, 2, 2, 3, 3
num_count = 0
num = 0
plus = 1
count = 1
arr = []

for tc in range(1, T+1):
    st, end = map(int, input().split())
    length = end - st

    # 데이터를 더 쌓자
    if num < length:
        while num < length:
            num += plus
            num_count += 1
            if num_count == 2:
                plus += 1
                num_count = 0

            arr.append((num, count))
            count += 1
        
        print(arr[-1][1])
    else:
        print(binarySearch(length))