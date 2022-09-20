import sys
sys.stdin = open("input.txt", "r")

dic = {'0':0000, '1':'0001', '2':'0010', '3':'0011', '4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
T = int(input())
for test_case in range(1, 2):
    N, M = map(int, input().split())
    # s = [input().strip() for _ in range(N)]
    s = sorted(list(set([input() for _ in range(N)])))
    s = s[1:]

    arr = []
    for row in s:
        print(row)

    # for i in range(len(s)):                 # 0 1
    #     for j in range(M):
    #         if s[i][j] in dic:
    #             arr.append(dic[s[i][j]])
    # arr = ("".join(map(str, arr)))
    # print(arr)

# 0001 1001 0110 1110 1011 1100 0101 1010 0011 0001 0110 1100 0101 0111 1000