import sys
sys.stdin = open("input.txt", "r")

def babyjin(lst):
    cnts = [0] * 12
    ans = 0
    for n in lst:
        cnts[n] += 1

    i = 0
    while i < 10:
        if cnts[i] >= 3:
            ans = 1
            break
        elif cnts[i] >= 1 and cnts[i + 1] >= 1 and cnts[i + 2] >= 1:
            ans = 1
            break
        i += 1
    return ans


T = int(input())
for test_case in range(1, T + 1):
    card = list(map(int, input().split()))
    player1 = []
    player2 = []
    winner = 0
    for i in range(len(card)):
        if i % 2 == 0:
            player1.append(card[i])
        else:
            player2.append(card[i])

        chk_player1 = babyjin(player1)
        chk_player2 = babyjin(player2)

        if chk_player1 == 1:
            winner = 1
            break
        elif chk_player2 == 1:
            winner = 2
            break

    print(f'#{test_case} {winner}')