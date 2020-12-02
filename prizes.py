

def prize_fond(count_participants, count_coins, fond_value):
    if count_participants == 1:
        return True
    value_for_participant = sum(fond_value) // count_participants
    if sum(fond_value) % count_participants > 0:
        return False
    fond_value.sort()
    x = 0
    result = []
    for i in range(1, count_coins + 1):
        while x != len(fond_value):
            if int(fond_value[x]) <= value_for_participant:
                result.append(fond_value[x])
                del fond_value[x]
                value_for_participant -= int(fond_value[x])
            x += 1
            if x >= len(fond_value) and value_for_participant != 0:
                return False
    return True


if __name__ == '__main__':
    k = int(input())
    n = int(input())
    fond = list(map(int, input().split(' ')))
    print(prize_fond(k, n, fond))