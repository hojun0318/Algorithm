import sys
sys.stdin = open("input.txt", "r")

# T = 10
T = int(input())
for test_case in range(1, T + 1):
    st = input()
    ans = cnt = 0
    for i in range(len(st)):
        if st[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if st[i - 1] == '(':        # 레이저
                ans += cnt
            else:
                ans += 1                # 막대기 끝

    print(f'#{test_case} {ans}')