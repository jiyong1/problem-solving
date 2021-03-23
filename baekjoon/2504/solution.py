dic = {')': '(', ']': '['}
c2num = {'(': 2, '[': 3}
stack = []

user_str = input()
current = 1
result = 0

for idx, c in enumerate(user_str):
    if c in c2num.keys():
        stack.append(c)
        current *= c2num[c]
    else:
        if not stack:
            result = 0
            break
        pre = stack.pop()

        if pre != dic[c]:
            result = 0
            break

        if user_str[idx-1] == pre:
            result += current
        
        current //= c2num[pre]

if stack:
    result = 0
    
print(result)