from django.shortcuts import render
import requests

from .utils.fetch_teams import create_teams
from .utils.fetch_news import parseHTML




def home(response):
    news = parseHTML("https://www.mlb.com/feeds/news/rss.xml")
    divisions = create_teams() 
    return render(response, "home.html", 
                  {'divisions':divisions, 
                    "news":news})

    
def team_hitters(request, id=id):
    team = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}").json()
    listTeam= team["teams"][0]
    division = listTeam["division"]["name"]
    teamstats = {}
    print(division)
    create_teams()
    # for i in range(create_teams()):
    #     print(i)
    # print(division)
    return render(request, "team_hitters.html", { "id":id }) 