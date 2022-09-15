import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    tc = int(input())
    queue = list(map(int, input().split()))

    while True:
        for i in range(1, 6):   # 사이클 : 1 ~ 5 감소
            ans = queue.pop(0) - i
            queue.append(ans)
            # 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료
            if ans <= 0:
                queue[-1] = 0   # 큐가 0 이하가 되면 큐의 마지막 값을 0으로 만든 후 Break
                ans = 0
                break
        # 탈출 조건
        if ans == 0:
            break

    print(f'#{tc}', *queue)