# 분해합

def getResult(current_sum, length, now_str):
    global flag
    if length < 0:
        global result
        if current_sum == N:
            result = now_str
            flag = True
            return

    else:
        for i in range(10):
            getResult(current_sum+i+(i*10**length), length-1, now_str+str(i))
            if flag:
                return



N = int(input())
result = ''
flag = False
getResult(0, len(str(N))-1, '')
if not result:
    result = 0
print(int(result))