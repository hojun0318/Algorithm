import sys
sys.stdin = open("input.txt", "r")

# def solve():
#     # [1] 수평으로 오목체크
#     for si in range(N):
#         for sj in range(N-5+1):     # 가능한 모든 위치
#             for d in range(5):
#                 if omok[si][sj + d] != 'o':
#                     break
#             else:
#                 return 'YES'
#
#     # [2] 수직으로 오목체크
#     for sj in range(N):
#         for si in range(N-5+1):     # 가능한 모든 위치
#             for d in range(5):
#                 if omok[si + d][sj] != 'o':
#                     break
#             else:
#                 return 'YES'
#
#     # [3] 대각선 하로 오목체크
#     for si in range(N-5+1):
#         for sj in range(N-5+1):     # 가능한 모든 위치
#             for d in range(5):
#                 if omok[si + d][sj + d] != 'o':
#                     break
#             else:
#                 return 'YES'
#
#     # [4] 대각선 상으로 오목체크
#     for si in range(4, N):
#         for sj in range(N-5+1):  # 가능한 모든 위치
#             for d in range(5):
#                 if omok[si - d][sj + d] != 'o':
#                     break
#             else:
#                 return 'YES'
#
#     return 'NO'

def check():
    for i in range(N):
        for j in range(N):
            for di, dj in move_point:
                for five in range(5):
                    ni, nj = i + di * five, j + dj * five       # 오목인지 check!
                    if 0 <= ni < N and 0 <= nj < N and omok[ni][nj] == 'o':
                        pass
                    else:
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    omok = [list(map(str, input())) for _ in range(N)]
    move_point = ((0, 1), (1, 0), (-1, 1), (1, 1))              # 우, 하, 대각선 상, 대각선 하

    # result = solve()
    result = check()

    print(f'#{test_case} {result}')
