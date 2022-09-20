import sys
sys.stdin = open("input.txt", "r")

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def get_binary(num):
    temps = []
    while True:
        quota = num // 2                   # 몫
        remainder = num % 2               # 나머지
        temps.append(remainder)
        num = quota
        if len(temps) == 4:
            break
    return temps
T = int(input())
for test_case in range(1, T + 1):
    N, s = map(str, input().split())
    s = list(s)                         # 리스트에 담기
    lst = []

    for i in range(len(s)):
        if s[i] in dic:
            s[i] = dic[s[i]]
    s = list(map(int, s))               # 리스트 속성을 문자열 -> 정수형

    for i in range(len(s)):
        num = get_binary(s[i])          # 리스트 각 원소들 2진수로 바꾸기
        num = num[::-1]                 # 2진수 비트를 역순을 저장

        for j in range(len(num)):
            lst.append(num[j])          # 2진수 비트로 바꾼 것들 모두 새로운 리스트에 저장
    lst = ("".join(map(str, lst)))

    print(f'#{test_case} {lst}')