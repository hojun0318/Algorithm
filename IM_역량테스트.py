import sys
sys.stdin = open("input.txt", "r")

def check():
    lst = list(set(grade))                          # 점수 중복 제거
    mn = -1
    ans = 1000000
    for i in range(len(lst) - 1):                   # T1, T2 모든 경우 확인
        for j in range(i + 1, len(lst)):
            T1 = lst[i]
            T2 = lst[j]
            A = []
            B = []
            C = []
            for k in grade:                         # T1, T2로 반 배정
                if k < T1:
                    C.append(k)
                elif T1 <= k < T2:
                    B.append(k)
                elif T2 <= k:
                    A.append(k)

            if Kmin <= len(A) <= Kmax and Kmin <= len(B) <= Kmax and Kmin <= len(C) <= Kmax:        # 인원 범위 안에 든다면
                x = abs(len(A) - len(B))
                y = abs(len(B) - len(C))
                z = abs(len(C) - len(A))
                for l in (x, y, z):
                    if l != 0:
                        if ans > l:
                            ans = l
                            mn = ans

    return mn


T = int(input())
for test_case in range(1, T  + 1):
    N, Kmin, Kmax = map(int, input().split())
    grade = list(map(int, input().split()))
    grade = sorted(grade)                           # 점수 오름차순

    result = check()

    print(f'#{test_case} {result}')