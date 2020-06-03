class League:
	def __init__(self, data):
		self.id = data["league_id"]
		self.name = data["name"]
		self.type = data["type"]
		self.country = data["country"]
		self.country_code = data["country_code"]
		self.season = data["season"]
		self.season_start = data["season_start"]
		self.season_end = data["season_end"]
		self.logo = data["logo"]
		self.flag = data["flag"]
		self.standings = data["standings"]
		self.is_current = data["is_current"]
		self.coverage = data["coverage"]
		self.id = data["league_id"]
		self.id = data["league_id"]
		self.id = data["league_id"]


# {
#     "league_id": 1,
#     "name": "World Cup",
#     "type": "Cup",
#     "country": "World",
#     "country_code": null,
#     "season": 2018,
#     "season_start": "2018-06-14",
#     "season_end": "2018-07-15",
#     "logo": "https://media.api-sports.io/football/leagues/1.png",
#     "flag": null,
#     "standings": 1,
#     "is_current": 1,
#     "coverage": {
#         "standings": true,
#         "fixtures": {
#             "events": true,
#             "lineups": true,
#             "statistics": true,
#             "players_statistics": true
#         },
#         "players": true,
#         "topScorers": true,
#         "predictions": true,
#         "odds": false
#     }
# },


