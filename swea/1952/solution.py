import sys
sys.stdin = open('input.txt')

T = int(input())
def getCost(current_cost, idx, mth):
    global my_min
    
    if current_cost > my_min:
        return
    if idx >= len(true_month) or mth > 12:
        if my_min > current_cost:
            my_min = current_cost
        return
    
    cmth = true_month[idx]
    if mth > cmth:
        getCost(current_cost, idx+1, mth)
    else:
        getCost(current_cost+tickets[0]*month[cmth], idx+1, cmth+1)

        getCost(current_cost+tickets[1], idx+1, cmth+1)

        getCost(current_cost+tickets[2], idx+1, cmth+3)

        getCost(current_cost+tickets[3], idx+1, 13)

for tc in range(1, T+1):
    tickets = list(map(int, input().split()))
    month = list(map(int, input().split()))
    true_month = [i for i in range(12) if month[i]]
    my_min = 40000

    getCost(0, 0, 0)

    print('#{} {}'.format(tc, my_min))