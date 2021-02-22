
def hanoi(fr, by, to, current):
    if current == 1:
        print(fr, to)
    else:
        hanoi(fr, to, by, current-1)
        print(fr, to)
        hanoi(by, fr, to, current-1)



# N = 원판의 개수
N = int(input())

# 이동 리스트
lst = []
count = 0

print(2**N-1)
if N <= 20:
    hanoi(1, 2, 3, N)