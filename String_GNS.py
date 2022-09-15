import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

table = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dict = {table[n]: n for n in range(10)}
# {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for test_case in range(1, T + 1):
    _, N = input().split()
    lst = list(input().split())

    # 입력 받은 숫자 카운트!
    cnt = [0] * 10
    for i in lst:
        cnt[dict[i]] += 1               # cnt[dict[ZRO]] -> cnt[0] += 1

    # 빈 문자열에 cnt 개수만큼 str 붙이기
    sols = ''
    for j in range(10):                                     # ex) j = 0
        sols += (table[j] + " ") * cnt[j]                   # (table[0] + " ") * cnt[0]         만약 cnt[0]이 5라면
                                                            # (ZRO + " ") * 5     -------->     ZRO ZRO ZRO ZRO ZRO
    print(f'#{test_case}')
    print(sols)