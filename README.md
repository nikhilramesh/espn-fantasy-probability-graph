# ESPN Fantasy Projection Graph


## Setup
1. Clone the repository
2. Install requirements with pip install -r requirements.txt

## Usage
To record projections live:

1. Replace the league ID variable in `run.py` with your desired league ID.
2. Run `python run.py` during the games. This will append the current projected score to a local CSV in the same directory with timestamps associated. You can stop and start this process whenever you want.

To plot the projection graphs:
1. Replace the league ID and filename variables with your desired league ID and the name of the CSV file with recorded projections.
2. Run `python plot.py` and see the magic happen. You can change the show_figures flag on line 67 of `plot.py` to True if you want to see the figures as you run the script. The script will automatically save them to a folder in the same directory.
