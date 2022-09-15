import sys
sys.stdin = open("input.txt", "r")

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:     # 부모가 없으면 root
            return i

def preorder(n):            # 전위 순회
    if n:
        lst.append(n)
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for test_case in range(1, T + 1):
    V = int(input())
    arr = list(map(int, input().split()))
    E = V - 1
    # 부모를 인덱스로 자식 번호 저장
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    # 자식을 인덱스로 부모 저장 확인
    par = [0] * (V + 1)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p

    lst = []
    root = find_root(V)
    preorder(root)
    print(f'#{test_case}', *lst)


