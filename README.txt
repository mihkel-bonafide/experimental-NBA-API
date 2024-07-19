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