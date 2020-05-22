from prettytable import PrettyTable


def print_leagues(leagues):
    menu = {}
    for l in leagues:
        print (l)
        menu[str(l['league_id'])] = l['name']
        print(str(l['league_id']) + " - " + str(l['name']) + " (" + str(l['country']) + ")")
    print("new - add league")
    return menu


def print_league(teams):
    R = "\033[0;31;40m"  # RED
    G = "\033[0;32;40m"  # GREEN
    Y = "\033[0;33;40m"  # Yellow
    B = "\033[0;34;40m"  # Blue
    N = "\033[0m"  # Reset
    t_league = PrettyTable(['#', 'Team', 'Points', 'P', 'W', 'D', 'L', "GD", "Status"])

    teams_copy = []
    for i, t in enumerate(teams):
        teams_copy.append(t)
        status = G + "Fine" + N
        if -1 < i < 4:
            status = B+"Champions League"+N
        if 3 < i < 7:
            status = Y+"Europa League"+N
        if i > 16:
            status = R+"Drop"+N
        t_league.add_row([t['rank'], t['name'],
                          t['points'], t['all']['matchsPlayed'],
                          t['all']['win'], t['all']['draw'],
                          t['all']['lose'], t['goalsDiff'],
                          status])
    print(t_league)
    return teams_copy


def print_team(t):
    print(t['name'])
    print(f"Founded - {t['founded']}. Logo - {t['logo']}")
    print(f"Stadium - {t['venue_name']}. Capacity - {t['venue_capacity']}")
    t_team = PrettyTable(['#', 'Team', 'Points', 'P', 'W', 'D', 'L', "GF", "GA", "GD"])
    t_team.add_row([t['rank'], t['name'], t['points'],
                      t['all']['matchsPlayed'], t['all']['win'],
                      t['all']['draw'], t['all']['lose'],
                      t['all']['goalsFor'], t['all']['goalsAgainst'], t['goalsDiff']])
    print(t_team)
    print(f"Last 5 matches - {t['forme']}")
    print("----------------------------------------------------------------------")


def print_fixtures(fixtures):
    t_fixture = PrettyTable(['Date', 'Home', 'GF', '-', 'GA', 'Away'])
    scores = []
    for match in fixtures:
        scores.append({'date': match['event_date'],
                       'team1': match['homeTeam']['team_name'],
                       'team1G': match['goalsHomeTeam'],
                       'team2': match['awayTeam']['team_name'],
                       'team2G': match['goalsAwayTeam']})
        t_fixture.add_row([match['event_date'], match['homeTeam']['team_name'],
                           match['goalsHomeTeam'], " - ",
                          match['goalsAwayTeam'], match['awayTeam']['team_name']])
    print(t_fixture)
    return scores
