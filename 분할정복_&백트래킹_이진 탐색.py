def bs(s, e, d):
    flag = 0  # 오른쪽: 1, 왼쪽: -1
    while s <= e:
        m = (s + e) // 2
        if alst[m] == d:  # 데이터를 찾은 경우
            return 1
        elif alst[m] < d:  # 데이터가 오른쪽에 있는 경우
            if flag == 1:
                return 0
            flag = 1  # 오른쪽 방문 표시
            s = m + 1
        else:  # 데이터가 왼쪽에 있는 경우
            if flag == -1:  # 연속 왼쪽 방문
                return 0
            flag = -1
            e = m - 1
    return 0  # 데이터를 못 찾은 경우


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))

    # 이진탐색은 반드시 lst 숫자 오름차순 정렬!!
    alst.sort()
    ans = 0
    for n in blst:
        ans += bs(0, len(alst) - 1, n)
    print(f'#{test_case} {ans}')