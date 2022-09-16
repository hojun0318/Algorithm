import sys
sys.stdin = open("input.txt", "r")

def preorder(n):
    if n:
        lst.append(n)
        preorder(son1[n])
        preorder(son2[n])

T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []

    son1 = [0] * (E + 2)
    son2 = [0] * (E + 2)

    par = [0] * (E + 2)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if son1[p] == 0:
            son1[p] = c
        else:
            son2[p] = c
        par[c] = p

    root = N
    preorder(root)
    print(f'#{test_case} {len(lst)}')