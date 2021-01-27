def red_in_blue(red, blue):
    rcx = int(red[0])
    rcy = int(red[1])
    rr = int(red[2])
    bminx = int(blue[0])
    bminy = int(blue[1])
    bmaxx = int(blue[2])
    bmaxy = int(blue[3])
    if rcx - rr < bminx or rcy - rr < bminy or rcx + rr > bmaxx or rcy + rr > bmaxy :
        return True
    else:
        return False

def blue_in_red(red, blue):
    rcx = int(red[0])
    rcy = int(red[1])
    rr = int(red[2])
    bminx = int(blue[0])
    bminy = int(blue[1])
    bmaxx = int(blue[2])
    bmaxy = int(blue[3])
    p1 = (bminx - rcx)**2 + (bminy - rcy) **2
    p2 = (bminx - rcx)**2 + (bmaxy - rcy) **2
    p3 = (bmaxx - rcx)**2 + (bminy - rcy) **2
    p4 = (bmaxx - rcx)**2 + (bmaxy - rcy) **2
    r2 = rr **2
    if p1 > r2 or p2 > r2 or p3 > r2 or p4 > r2:
        return True
    else:
        return False



def main():
    T = int(input())
    for t in range(1, T+1):
        red_list = input().split(' ')
        blue_list = input().split(' ')
        result = f'#{t} '
        if red_in_blue(red_list, blue_list):
            result += 'Y'
        else:
            result += 'N'
        if blue_in_red(red_list, blue_list):
            result += 'Y'
        else:
            result += 'N'
        
        print(result)

if __name__ == '__main__':
    main()