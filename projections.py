import os
from datetime import datetime

import pandas as pd
from espn_api.football import League


def get_league(league_id: int, year: int):
    return League(league_id, year)

def get_current_projected_scores(league: League):
    league.refresh()
    projected = {}
    for box in league.box_scores():
        projected[box.home_team.team_name] = [box.home_projected]
        projected[box.away_team.team_name] = [box.away_projected]
    return projected

def store_projected_scores(filename, projected_scores: dict):
    df = pd.DataFrame.from_dict(projected_scores, orient='columns')
    df['TIMESTAMP'] = str(datetime.now())
    
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, mode='a', index=False)

