result = 0
def getResult(energy, score):
    if len(energy) == 2:
        global result
        # print(score)
        if result < score:
            result = score
    
    else:
        current = energy[:]
        for idx, num in enumerate(current):
            if idx == 0 or idx == len(current)-1:
                continue
            now_score = current[idx-1] * current[idx+1]
            current.pop(idx)
            getResult(current, score+now_score)
            current.insert(idx, num)


N = int(input())
energy = [int(i) for i in input().split()]
getResult(energy, 0)
print(result)