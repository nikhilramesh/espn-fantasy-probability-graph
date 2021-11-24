import os
from dateutil import parser

import pandas as pd
import matplotlib.pyplot as plt

import projections


league_id = 1341130
league_year = 2021
filename = '1341130_week12.csv'


def get_scores_by_team(filename, league):
    df = pd.read_csv(filename)
    historical_projected = {}
    for team in league.teams:
        timestamps = list(df['TIMESTAMP'])
        scores = list(df[team.team_name])
        historical_projected[team.team_name] = scores
    return historical_projected, timestamps


def get_matchups(league):
    return league.scoreboard()


def get_team_names_from_matchup(matchup):
    team_1 = matchup.home_team.team_name
    team_2 = matchup.away_team.team_name
    return team_1, team_2


def plot_and_save_matchup(team_1, team_2, scores, timestamps, directory, show_figures=False):
    team_1_scores = scores[team_1]
    team_2_scores = scores[team_2]
    parsed_timestamps = [parser.parse(t) for t in timestamps]

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(parsed_timestamps, team_1_scores, label=team_1)
    ax.plot(parsed_timestamps, team_2_scores, label=team_2)

    ax.set_title("Projected Scores")

    plt.ylim([0, 200])
    plt.xlabel('Time')
    plt.ylabel('Score')

    plt.savefig(f"{directory}/{team_1}_{team_2}.jpg")

    if show_figures:
        plt.legend()
        plt.show()


def plot_and_save_all_matchups():
    league = projections.get_league(league_id, league_year)
    matchups = get_matchups(league)
    scores, timestamps = get_scores_by_team(filename, league)

    directory = f"{filename.split('.')[0]}_graphs"
    os.makedirs(directory, exist_ok=True)

    for matchup in matchups:
        team_1, team_2 = get_team_names_from_matchup(matchup)
        plot_and_save_matchup(team_1, team_2, scores, timestamps, directory, show_figures=False)


if __name__ == "__main__":
    plot_and_save_all_matchups()
