
result = 0
def isLucky(str_list):
    for idx in range(len(str_list)-1):
        if str_list[idx] == str_list[idx+1]:
            return False

    return True

def next_permutation(str_list):
    i, j = len(str_list)-1 ,len(str_list)-1

    while i>0 and str_list[i-1]>=str_list[i]:
        i-=1

    if i==0:
        return False
    
    while str_list[i-1] >= str_list[j]:
        j -= 1
    
    str_list[i-1], str_list[j] = str_list[j], str_list[i-1]

    k = len(str_list)-1

    while i<k:
        str_list[i], str_list[k] = str_list[k], str_list[i]
        i += 1
        k -= 1
    return str_list

    

text = list(input())
text.sort()
if isLucky(text):
    result += 1
# next_permutation(text)
while(next_permutation(text)):
    if isLucky(text):
        result += 1

print(result)
