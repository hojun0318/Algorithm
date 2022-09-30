import sys
sys.stdin = open("input.txt", "r")

di = (1, -1, 0, 0)
dj = (0, 0, -1, 1)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # [0] 각 원자 i,j좌표 *2, 그리고 1씩 이동 -> 좌표 중간에서 충돌하는 경우도 처리 가능
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2

    ans = 0
    # 4001번 루프: 가장 멀리 있는 원자가 충돌할 경우
    for _ in range(4001):
        # [1] 좌표 1칸 이동
        for i in range(len(arr)):
            arr[i][0] += dj[arr[i][2]]
            arr[i][1] += di[arr[i][2]]

        # [2] 같은 좌표인 경우 del리스트에 추가
        v = []
        ddel = set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj, ci) not in v:  # 없는 경우 추가
                v.append((cj, ci))
            else:  # 있다면 제거 대상
                ddel.add((cj, ci))

        # [3] ddel리스트에 있는 원자 삭제 및 에너지 누적
        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)

        for i in range(1, len(arr)):
            if arr[i][2] != arr[i - 1][2]:
                break
        else:
            break  # 모든 원자의 방향이 같음

        if len(arr) < 2:
            break

    print(f'#{test_case} {ans}')