import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count = [0] * 201

    # 시작 부터 끝점까지 각각  count를 올린다
    # 그럼 겹치는 횟수가 각 복도에 나올 것이고
    # 이의 최대 값이 곧 걸리는 시간이 된다.
    result = 0

    for _ in range(N):
        start, end = map(int, input().split())
        
        # 1-2 같은 라인 3-4 같은 라인
        # 즉 홀수면 //2+1, 짝수면 //2
        start = start//2 + 1 if start%2 else start//2
        end = end//2 + 1 if end%2 else end//2

        if start > end:
            start, end = end, start

        for i in range(start, end+1):
            count[i] += 1
            if result < count[i]:
                result = count[i]
    

    print('#{} {}'.format(tc, result))

            
            


        
    