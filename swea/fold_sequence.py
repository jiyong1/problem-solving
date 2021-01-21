# 접을 수 있느냐?
# 없다면 전에 접었던 것은 성공했느냐 했다면 return/ 못했다면 하나 더 지우는 것으로 가자
# 원소 두개 남긴다면 length C length-2 가 경우의 수, 길이는 2

def getResult(erase):
    global visited

    if length - erase == 2:
        return 2, length*(length-1)/2
    elif length <= 1:
        return 0, 1
    else:
        # 접을 수 없는가?
        if (length - erase)%2 == 1:
            if count != 0:
                return length-erase+1, count
            else:
                visited = [False for i in range(length)]
                # getResult



visited = []
length = 0
count = 0
lst = []
T = int(input())
for t in range(1, T+1):
    length = int(input())
    visited = [False for i in range(length)]
    count = 0
    input_str = input().split(' ')
    lst = [int(i) for i in input_str]
    slong, num = getResult()
    print(f'#{t} {slong} {num}')
    # getResult(0)
    print(visited)
    