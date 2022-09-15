for test_case in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N - 2):

        if lst[i] > lst[i - 1] \
            and lst[i] > lst[i - 2] \
            and lst[i] > lst[i + 1] \
            and lst[i] > lst[i + 2]:

            b1 = lst[i] - lst[i - 2]
            b2 = lst[i] - lst[i - 1]
            b3 = lst[i] - lst[i + 1]
            b4 = lst[i] - lst[i + 2]
            min_b = b1
            for b in [b1, b2, b3, b4]:
                if b < min_b:
                    min_b = b
            cnt += min_b
    print(f'#{test_case} {cnt}')