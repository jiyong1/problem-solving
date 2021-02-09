import sys
sys.stdin = open("input.txt")

T = int(input())

def getGravitation(x, idx, isLeft):
    # x => 물체 좌표 / idx 시작 인덱스 / 왼쪽인가?
    result = 0
    if isLeft:
        for i in range(idx, -1, -1):
            distance = x - x_list[i]
            result += m_list[i]/(distance*distance)
        return result
    else:
        for j in range(idx, count):
            distance = x_list[j] - x
            result += m_list[j]/(distance*distance)
        return result



for tc in range(1, T+1):
    count = int(input())
    input_list = list(map(int, input().split()))
    x_list = input_list[:count]
    m_list = input_list[count:]
    result_string = ''
    for i in range(count-1):
        st = x_list[i]
        end = x_list[i+1]
        mid = (st + end)/2
        fl = getGravitation(mid, i, True)
        fr = getGravitation(mid, i+1, False)
        while end - st > 1e-12:
            if fr > fl:
                end = mid
            else:
                st = mid

            pre = mid
            mid = (st+end)/2
            # if '%0.12f' % pre == '%0.12f' % mid:
                # mid = pre
                # break
            fl = getGravitation(mid, i, True)
            fr = getGravitation(mid, i+1, False)
        result_string += ' {:.10f}'.format(mid)


    print("#{}{}".format(tc, result_string))

