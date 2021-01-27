# 1. 16진수 2진수로 변환 -> 스트링 판별 필요함

# 2. 2진수로 블럭단위 나눠서 0~9판단

# 

number_block = {'3211' : 0, '2221' : 1, '2122' : 2, '1411' : 3, '1132' : 4, '1231' : 5, '1114' : 6, '1312' : 7, '1213' : 8, '3112' : 9}


T = int(input())
for t in range(1, T+1):
    row_col = list(map(int, input().split()))
    hex_list = []
    zero_string = '0'*row_col[1]
    pre = ''
    for _ in range(row_col[0]):
        result = 0
        n_string = input()
        if n_string == zero_string or n_string == pre:
            continue
        else:
            pre = n_string
            tmp = ''
            for char in n_string:
                if char == '0' and tmp:
                    if not tmp in hex_list:
                        hex_list.append(tmp)
                    tmp = ''
                else:
                    tmp += char
    
    print(hex_list)
            


