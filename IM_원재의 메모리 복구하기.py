import sys
sys.stdin = open("input.txt", "r")

def fix():
    memory = [0] * len(target)                  # 초기화 메모리
    cnts = 0
    for i in range(len(target)):
        if target == memory:                    # target 리스트와 같게도면 중단
            break
        if target[i] != memory[i]:              # 각 요소 순환하는데 다르면
            cnts += 1                           # 횟수 1 증가
            for j in range(i, len(target)):     # 마지막 요소까지 변경
                memory[j] = (1 - memory[j])
    return cnts


T = int(input())
for test_case in range(1, T + 1):
    target = list(map(int, input()))

    ans = fix()

    print(f'#{test_case} {ans}')