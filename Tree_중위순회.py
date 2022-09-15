import sys
sys.stdin = open("input.txt", "r")

def inorder(N):
    if N:
        inorder(son1[N])
        print(alpabat[N], end='')
        inorder(son2[N])

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    son1 = [0] * (N + 1)
    son2 = [0] * (N + 1)
    alpabat = [''] * (N + 1)
    root = 1

    for i in range(1, N + 1):
        lst = list(input().split())
        alpabat[i] = lst[1]
        if len(lst) == 4:
            son1[i] = int(lst[2])
            son2[i] = int(lst[3])
        if len(lst) == 3:
            son1[i] = int(lst[2])

    while son1[root] == 0 and son2[root] == 0:
        root += 1
    print(f'#{test_case}', end=' ')
    inorder(root)
    print()



