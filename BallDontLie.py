import os
import requests
import json
from dotenv import load_dotenv

"""
This program uses the "BallDontLie" API and (at this stage) executes calls on two different endpoints. The first
hits the "https://api.balldontlie.io/v1/players" endpoint and utilizes user input (unsanitized as of now) to
construct a query-string that pulls an individual NBA player's "player_id", which then gets passed to the 
endpoint located at https://api.balldontlie.io/v1/season_stats (this endpoint can't be queried by name, you need 
that player ID). The 2nd endpoint's data is parsed and sent to a display module, which shows the user's selected 
player's stats for the 2023-2024 season. This isn't intended for any other purpose beyond my own personal 
development/experience in working with different public APIs.

Note: this program's reliance on querystrings bears no real significance beyond me randomly choosing that method; the 
moment I was able to get this code to execute successfully was the same moment I wished I'd used parameters or payloads
instead. :)  -MPG, 7.18.24

"""

def find_player(): 
    player_search = input(f"Please type the name of the NBA player you wish to search: ")
    first, last = player_search.split(' ', 1)
    querystring = "https://api.balldontlie.io/v1/players?first_name=" + first + "&" + "last_name=" + last
    # print(querystring)  # confirm querystring format
    retrieve_id(querystring)

def retrieve_id(player):
    load_dotenv()  
    api_key = os.getenv("BDL_API_KEY")   

    url = player
    payload = {}
    headers = {'Authorization': api_key}

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonify = response.json()
    one_object_array = jsonify["data"]
    opus = one_object_array[0]
    id = opus["id"]
    retrieve_player_data(id)

def retrieve_player_data(player_id):
    load_dotenv()  
    api_key = os.getenv("BDL_API_KEY")   
    id = str(player_id)
    url = "https://api.balldontlie.io/v1/season_averages?season=2023&player_ids[]=" + id
    payload = {}
    headers = {'Authorization': api_key}

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonify = response.json()  # produces array with one index item for selected player
    one_object_array = jsonify["data"]  # strips "data" so we're left with the values (but still encapsulated as an array)
    opus = one_object_array[0]  # converts the 1-item array into a dictionary with key:value pairs
    # print(opus)  # confirms data format
    display_data(opus)

def display_data(player_stats):
    print(f"Points per game: {player_stats['pts']}")
    print(f"Assists per game: {player_stats['ast']}")
    print(f"Rebounds per game: {player_stats['reb']}")
    print(f"Steals per game: {player_stats['stl']}")
    print(f"Blocks per game: {player_stats['blk']}")
    print(f"Turnovers per game: {player_stats['turnover']}")
    print(f"Field goals made/attempted/%: {player_stats['fgm']}/{player_stats['fga']}: {player_stats['fg_pct']:.1%}")
    print(f"Free-throws made/attempted/%: {player_stats['ftm']}/{player_stats['fta']}: {player_stats['ft_pct']:.1%}")
    print(f"3-point shots made/attempted/%: {player_stats['fg3m']}/{player_stats['fg3a']}: {player_stats['fg3_pct']:.1%}")
    print(f"Games played in 2023: {player_stats['games_played']}")
    print(f"BDL Player ID: {player_stats['player_id']}")

def main(): 
    print(f"Welcome to the NBA player analytics tool!")
    print() 
    find_player()

main() 
