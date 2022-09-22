import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())        # N: 컨테이너 개수, M: 트럭 개수
    wi = list(map(int, input().split()))    # wi: 화물의 무게
    ti = list(map(int, input().split()))    # ti: 트럭 적재 용량
    ans = 0

    # [1] 둘 다 내림차순 정렬
    wi.sort(reverse=True)
    ti.sort(reverse=True)

    # [2] 화물을 하나씩 내리면서 트럭에 적재 가능한지 체크
    i = 0
    for weight in wi:               # 화물을 하나씩 내림
        if weight <= ti[i]:         # 트럭에 가능한 경우
            ans += weight
            i += 1
            if i == M:
                break

    print(f'#{test_case} {ans}')