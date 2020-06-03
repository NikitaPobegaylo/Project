#!/usr/bin/env python3


# https://rapidapi.com/api-sports/api/api-football?endpoint=apiendpoint_7a821242-d84f-499d-a35a-7d0079ba4228

# headers = {
#     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
#     "X-RapidAPI-Key": "a0adcd28ffmsh29f567331ce0cbap143ac2jsn5ffb61a1b960"
# }

headers = {
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "9373ea7cd6msh86f898bca984655p13a552jsn5d9a680330f8"
}

url = lambda path: "https://api-football-v1.p.rapidapi.com/v2/{path}".format(path = path)


if __name__ == "__main__":
	print(headers)
	print(url())
