
def getMin(bit, st_count):
    global result
    if st_count >= N//2:
        start = []
        link = []
        for i in range(N):
            if bit & (1<<i):
                start.append(i)
            else:
                link.append(i)
        
        st_score = 0
        li_score = 0

        for i in range(N//2):
            st1 = start[i]
            li1 = link[i]
            for j in range(i+1, N//2):
                st2 = start[j]
                li2 = link[j]
                st_score += arr[st1][st2] + arr[st2][st1]
                li_score += arr[li1][li2] + arr[li2][li1]

        if result > abs(st_score-li_score):
            result = abs(st_score-li_score)

        visited[bit] = True
        visited[((1<<N)-1) ^ bit] = True
    else:
        for i in range(N):
            if visited[bit|(1<<i)] or pick[i]:
                continue
            pick[i] = True
            getMin(bit|(1<<i), st_count+1)
            pick[i] = False

        visited[bit] = True

        


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
result = 2000
visited = [False for _ in range(1<<N)]
pick = [False for _ in range(N)]

getMin(0, 0)

print(result)