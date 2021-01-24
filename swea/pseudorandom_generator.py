# 1. 테스트 케이스

# 2. s p q m 으로 식을 만들어야 하겠지?

# 3. 무한 반복으로 리스트를 계속해서 만들자

# 4. 리스트를 만들고 현재 끝 인덱스 부터 서브 리스트를 만들어 비교하자

# 5. 비교 어떻게 할까?

# 시간 초과이다..

# 그렇다면 모듈러 연산의 특징을 활용하여 문제를 풀어보자

# 두번째 풀이

# 리스트 만들어서 리스트에 카운트를 넣어준다 왜냐 어차피 모듈러 연산이기 때문에 

# 한번 나온 수가 다시 나오는 형태는 주기로 돌아왔을 때일 뿐이다.

# 리스트 만들면 시간을 좀 더 덜 쓰지 않을까 했는데.. 그게 안되네 100개중 73개를 맞음

# 세번째 풀이

# 딕셔너리로 바꿔서 참조하는 형태로 해봤더니 87개 맞았다.. 시간초과야 어디서 줄일 수 있니?



def Pseudorandom_func(p, q, m, pre):
    return (p*pre + q) % m

def main():
    T = int(input())
    for t in range(1, T+1):
        input_str = input()
        str_list = input_str.split(' ')
        s = int(str_list[0])
        p = int(str_list[1])
        q = int(str_list[2])
        m = int(str_list[3])

        psr_dict = {s:1}
        pre = s
        count = 1
        result = 0
        while True:
            count += 1
            now = Pseudorandom_func(p, q, m, pre)
            if now in psr_dict:
                result = count - psr_dict[now]
                break
            psr_dict[now] = count
            pre = now
            
        print(f'#{t} {result}')

if __name__ == "__main__":
    main()
