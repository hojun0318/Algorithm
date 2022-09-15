import sys
sys.stdin = open("input.txt", "r")

def inorder(n):
    global cnt

    if n <= N:              # 존재하는 노드인 경우 처리
        inorder(n * 2)        # Left
        lst[n] = cnt
        cnt += 1
        inorder(n * 2 + 1)    # Right

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    # 완전이진트리 생성
    cnt = 1
    inorder(1)

    print(f'#{test_case} {lst[1]} {lst[N // 2]}')