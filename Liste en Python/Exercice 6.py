from random import randint


def main():
    li = ['1', '2', '3', '4', '5', '6']
    player = len(li) // 2

    team_1 = []
    team_2 = []

    for i in li:
        if (
            randint(1, 2) == 1
            and len(team_1) < player
            or randint(1, 2) != 1
            and len(team_2) >= player
        ):
            team_1.append(i)
        else:
            team_2.append(i)

    print(f"équipe 1: {team_1}")
    print(f"équipe 2: {team_2}")

if __name__ == '__main__':
    main()