#!/usr/bin/env python3

from api.teams import *
from api.leagues import *
from api.stats import *
import db.queries as db
import pymongo
import ui.print_menu as ui
from statsmodels.tsa.arima_model import ARMA
import matplotlib.pyplot as plt
import numpy as np

client = pymongo.MongoClient("mongodb://localhost:27100/")
my_db = client["cw_db"]
col_t = my_db["teams"]
col_l = my_db["leagues"]
col_s = my_db["standings"]


def forecast(matches):
    example = matches[0]
    for i, m in enumerate(matches):
        if m['team1'] != example['team1']:
            temp = m['team1']
            matches[i]['team1'] = m['team2']
            matches[i]['team2'] = temp
            temp = m['team1G']
            matches[i]['team1G'] = m['team2G']
            matches[i]['team2G'] = temp
    data1 = []
    data2 = []
    for m in matches:
        if m['team1G'] is not None:
            data1.append(m['team1G'])
            data2.append(m['team2G'])
    try:
        model1 = ARMA(data1, order=(0, 1))
        model_fit1 = model1.fit(disp=False)
        # make prediction
        yhat1 = model_fit1.predict(len(data1), len(data1))

        model2 = ARMA(data2, order=(0, 1))
        model_fit2 = model2.fit(disp=False)
        # make prediction
        yhat2 = model_fit2.predict(len(data2), len(data2))
        print(f"{example['team1']}: {round(yhat1[0])} ({round(yhat1[0], 4)}) - ({round(yhat2[0], 4)}) {round(yhat2[0])} :{example['team2']}")
    except ValueError:
        print("Sorry there is not enough data to make a forecast")
    return matches


def create_graph(matches):
    x = []
    y = []
    for m in matches:
        if m['team1G'] is not None:
            x.append(m['team1G'])
            y.append(m['team2G'])
    data = np.column_stack((x, y))

    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2,
        figsize=(8, 4)
    )
    ax2.hist(
        data, bins=np.arange(data.min(), data.max()),
        label=(f"{matches[0]['team1']}", f"{matches[0]['team2']}")
    )

    ax2.legend(loc=(0.65, 0.8))
    ax2.set_title('Frequencies of $x$ and $y$')
    ax2.yaxis.tick_right()

    plt.show()


def run_h2h(team, option):
    while True:
        team2 = db.get(col_t, {"name": {"$regex": "^" + option}})
        if team2 is None:
            print("Sorry, there is no such team. Try again")
            break
        h2h = get_h2h(team['team_id'], team2['team_id'])

        print("----------------------------------------------------------------------")
        if len(h2h) is 0:
            print("Teams haven't faced yet")
        matches = ui.print_fixtures(h2h)
        print("Match result forecast")
        fixtures = forecast(matches)

        option = input("s - to generate graphic. q - to exit: ")
        print(option)
        if option is 'q':
            break
        if option is 's':
            create_graph(fixtures)
        else:
            print("----------------------------------------------------------------------")
            print("No such option, try again...")


def team_select(teams):
    while True:
        teams = ui.print_league(teams)
        team_name = input("Enter team to see detailed statistics: ")
        if team_name is 'q':
            break
        print("----------------------------------------------------------------------")
        team = db.get(col_t, {"name": {"$regex": "^"+team_name}})
        if team is None:
            print("Sorry, there is no such team in this league. Try again")
        else:
            while True:
                ui.print_team(team)
                option = input("Enter another team to see Head-to-head or press \'q\' to come back: ")

                if option is 'q':
                    break
                run_h2h(team, option)


while True:
    print("----------------------------------------------------------------------")
    leagues = db.get_all(col_l)
    menu = ui.print_leagues(leagues)

    print("----------------------------------------------------------------------")
    option = input("Choose league...: \n")
    if option is 'q':
        break

    # if option is 'new':
    #     # get league

    # if option is 'docs':
    #     get docs

    if option in menu:
        if menu[option] == "Bundesliga 1":
            menu[option] = "Bundesliga"
        if menu[option] == "Primera Division":
            menu[option] = "Primera División"
        teams = db.get_all(col_t, {'group': menu[option]}, "rank")
        team_select(teams)
    else:
        print("----------------------------------------------------------------------")
        print("No such option, try again...")
