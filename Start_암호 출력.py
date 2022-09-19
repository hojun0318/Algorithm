import sys
sys.stdin = open("input.txt", "r")

def get_binary(n):
    temps = []
    while True:
        quota = n // 2
        remainder = n % 2
        temps.append(remainder)
        n = quota
        if len(temps) == 4:
            break
    return temps


dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
secret_code = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

T = int(input())
for test_case in range(1, 2):
    s = list(map(str, input()))
    lst = []

    for i in range(len(s)):
        if s[i] in dic:
            s[i] = dic[s[i]]
    s = list(map(int, s))

    for i in range(len(s)):
        num = get_binary(s[i])
        num = num[::-1]
        for j in range(len(num)):
            lst.append(num[j])
    lst = ("".join(map(str, lst)))
    print(lst)

    for i in range(len(lst) - 6):
        ans = []
        for j in range(6):
            ans.append(lst[i + j])
        ans = ("".join(map(str, ans)))
        print(ans)
        if ans in secret_code:
            print(secret_code[ans])
        print(ans)
    # values = int(lst[0])
    # ans = []
    # for i in range(1, len(lst)):
    #     values = values * 2 + int(lst[i])
    #     if i % 7 == 6:
    #         ans.append(values)
    #         values = 0
    # ans.append(values)
    #
    # print(f'#{test_case}', *ans)