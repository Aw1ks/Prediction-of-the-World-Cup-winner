import itertools
import random


def simulate_group(group, n_iterations=1000):
    scores = {team: 0 for team in group.keys()}
    teams = list(group.keys())
    matches = list(itertools.combinations(teams, 2))

    for _ in range(n_iterations):
        for match in matches:
            team1 = match[0]
            team2 = match[1]
            team1_lvl = group[team1]
            team2_lvl = group[team2]

            p1 = team1_lvl / (team1_lvl + team2_lvl)

            if random.random() < p1:
                scores[team1] += 3
            else:
                scores[team2] += 3

    scores = {key: value / n_iterations for key, value in scores.items()}

    places = {team: place + 1 for place, (team, _) in enumerate(sorted(scores.items(), key=lambda x: x[1], reverse=True))}
    print(f'{places}\n')

    return places, scores


def final_groups(group_1, group_2, place_1, place_2):
    filtered_group_1 = {key: value for key, value in group_1.items() if value == place_1}
    filtered_group_2 = {key: value for key, value in group_2.items() if value == place_2}

    merged_group = {*filtered_group_1, *filtered_group_2}
    print(f'{merged_group}')

    return merged_group


def top_three_teams(rezult1, rezult2, scores_group_1, scores_group_2):
    all_teams = rezult1.union(rezult2)

    all_scores = {}
    for team in all_teams:
        score = 0
        if team in scores_group_1:
            score += scores_group_1[team]
        if team in scores_group_2:
            score += scores_group_2[team]
        all_scores[team] = score

    sorted_teams = sorted(all_scores.items(), key=lambda x: x[1], reverse=True)

    teams, _ = zip(*sorted_teams[:3])
    print(teams)
    print(f'Победитель {teams[0]}')
    print(f'Второе место {teams[1]}')
    print(f'Третье место {teams[2]}')


def main():
    gruppa_d = {'Франция': 85, 'Дания': 65, 'Австралия': 55, 'Тунис': 20}
    gruppa_e = {'Германия': 85, 'Япония': 65, 'Испания': 85, 'Коста-Рика': 55}

    print('Группа d')
    filter_group_1, scores_group_1 = simulate_group(gruppa_d)

    print('Группа e')
    filter_group_2, scores_group_2 = simulate_group(gruppa_e)

    print('Финал')
    rezult1 = final_groups(filter_group_1, filter_group_2, 1, 2)
    rezult2 = final_groups(filter_group_1, filter_group_2, 2, 1)

    top_three_teams(rezult1, rezult2, scores_group_1, scores_group_2)


if __name__ == '__main__':
    main()