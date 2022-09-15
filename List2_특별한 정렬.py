import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N - 1):          # 선택정렬로 내림차순 만들기
        maxIndex = i
        for j in range(i + 1, N):
            if lst[maxIndex] < lst[j]:
                maxIndex = j
        lst[i], lst[maxIndex] = lst[maxIndex], lst[i]

    sols = []
    for i in range(5):
        sols.append(lst[i])
        sols.append(lst[-1-i])

    print(f'#{test_case}', *sols)