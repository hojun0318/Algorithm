import sys
sys.stdin = open("input.txt", "r")


def postorder(n):
    global ans
    if n <= N:
        postorder(n * 2)
        postorder(n * 2 + 1)
        ans += arr[n]

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())  # N: 노드의 개수, M: 리프 노드의 개수, L: 출력 노드 번호
    arr = [0] * (N + 1)
    par = [0] * (N + 1)
    ans = 0

    for i in range(M):
        num_leaf, num = map(int, input().split())   # num_leaf: 리프 노드 번호, num: 자연수
        arr[num_leaf] = num

    postorder(L)
    print(f'#{test_case}', ans)