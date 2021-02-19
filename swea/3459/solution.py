import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    # 0 : alice / 1 : bob
    result = 1

    start = 1
    mul = 1
    both = False

    while N > start:
        result = 1 if result == 0 else 0

        if not both:
            both = True
            mul *= 4
        else:
            both = False


        start += mul


    if result == 0:
        result = 'Alice'
    else:
        result = 'Bob'

    print("#{} {}".format(tc, result))
