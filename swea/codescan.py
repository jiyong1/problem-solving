import sys
sys.stdin = open("input.txt")

T = int(input())
code = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}
hex2bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def isNormal(code):
    num = ((code[1] + code[3] + code[5] + code[7]) * 3) + code[2] + code[4] + code[6] + code[0]
    if num % 10 == 0:
        return True
    else:
        return False


for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw_code = [input()[:M] for _ in range(N)]
    visited = []
    result = 0
    # 1. 16진수로 구성되어 있는 현재 코드를 이진화한다.
    for i in range(N):
        tmp_bin = ''
        for char in raw_code[i]:
            tmp_bin += hex2bin[char]
        # 2. raw data -> binary data
        raw_code[i] = tmp_bin

    # 3. 1이 없으면 continue, 있다면 이진 코드 -> 숫자
    # 4. 숫자 8개 얻어냈다? -> 검정 !
    for i in range(N):
        if not '1' in raw_code[i]:
            continue
        # 5. 이진 코드로 숫자를 얻어내보자 두깨는 랜덤인데 어차피 비율로 따질 테니 제일 최소의 수로 나누면 되지
        numbers = []
        first = second = third = 0
        for j in range(M*4-1, -1, -1):
            # 6. 1의 첫 등장
            if second == third == 0 and raw_code[i][j] == '1':
                first += 1
            # 7. 1 앞에 0이 나오면 두번째 블럭이라 보면 됨
            elif first != 0 and third == 0 and raw_code[i][j] == '0':
                second += 1
            # 8. second 블럭 이후에 1이 등장하면 세번째 블럭이지
            elif second != 0 and first != 0 and raw_code[i][j] == '1':
                third += 1
            # 9. third 블럭 이후 0이 등장한다면 숫자로 변환 해보고 8개 숫자 쌓이면 유효 코드 검증!
            # 10. 초기화 필수 ! -> 숫자 리스트 빈리스트로 초기화 / visited 안에 숫자 넣어주기
            elif first != 0 and second != 0 and third != 0 and raw_code[i][j] == '0':
                cri = min(first, second, third)
                code_key = str(third//cri) + str(second//cri) + str(first//cri)
                numbers.append(code[code_key])
                # 다시 다음 숫자를 얻어내기 위해서 3가지 블럭 초기화 해줘야함
                first = second = third = 0
                # 8개의 숫자가 모였다!
                if len(numbers) == 8:
                    # 이미 검사한 코드라면 넘기자
                    if not numbers in visited:
                        if isNormal(numbers):
                            result += sum(numbers)
                        visited.append(numbers)
                    # 검사했든 안했든 8개모인거 확인했으니 numbers 초기화
                    numbers = []

    print("#{} {}".format(tc, result))

