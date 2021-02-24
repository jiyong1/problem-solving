# 각 순열에서 오른쪽만 바라본다.
# 맨 오른쪽 부터 탐색을 시작한다.
# 스택에 나보다 큰게 보일 때까지 스택을 비운다
# 왜 가능한가? 어차피 내가 제일 큰놈이라면 내 바로 왼쪽에서도 나를 볼거야

# N = 수열의 길이

N = int(input())

permutation = list(map(int, input().split()))

# 오른쪽에 나보다 큰 놈을 확인하기 위해서
right_stack = []

# 맨 마지막은 -1
result = [-1]

right_stack.append(permutation[-1])

# 뒤에서 두번째부터 0 까지
for i in range(len(permutation)-2, -1, -1):
    current = permutation[i]
    now = -1

    while right_stack and right_stack[-1] <= current:
        right_stack.pop()

    if right_stack:
        now = right_stack[-1]

    right_stack.append(current)

    result.append(now)


print(' '.join(map(str, result[::-1])))

