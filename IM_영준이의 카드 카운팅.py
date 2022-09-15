import sys
sys.stdin = open("input.txt", "r")

dic = {'S': 0, 'D': 1, 'H': 2, 'C': 3}

T = int(input())
for test_case in range(1, T + 1):
    st = input()
    lst = [[] for _ in range(4)]
    # [1] lst의 해당 무늬(번호) 카드번호 추가
    for i in range(0, len(st), 3):
        num = int(st[i + 1: i + 3])
        lst[dic[st[i]]].append(num)

    ans = []
    for i in range(4):
        if len(lst[i]) != len(set(lst[i])):
            print(f'#{test_case} ERROR')
            break
        else:
            ans.append(13-len(lst[i]))
    else:
        print(f'{test_case}', *ans)