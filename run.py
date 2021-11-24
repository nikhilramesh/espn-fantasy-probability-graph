from time import sleep

import projections

league_id = 1341130
league_year = 2021

def run():
    league = projections.get_league(league_id, league_year)
    filename = f"{str(league_id)}_week{str(league.current_week)}.csv"
    while True:
        scores = projections.get_current_projected_scores(league)
        projections.store_projected_scores(filename, scores)
        print("Stored projected scores:", scores)
        sleep(3)

if __name__ == "__main__":
    run()