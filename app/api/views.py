from django.shortcuts import render
import requests

from .utils.fetch_teams import create_teams
from .utils.fetch_news import parseHTML
from .utils.team_details import team_details
from .utils.get_hitters import get_hitters
from .utils.get_pitchers import get_pitchers




def home(response):
    news = parseHTML("https://www.mlb.com/feeds/news/rss.xml")
    divisions = create_teams() 
    print(divisions[0]["div"][0])
    return render(response, "home.html", 
                  {'divisions':divisions, 
                    "news":news})

    
def team_hitters(request, id=id):
    teamdetails = team_details(id)
    players = get_hitters(id) 
    return render(request, "team_hitters.html", { "id":id, "team":teamdetails, "players":players }) 

def team_pitchers(request, id=id):
    teamdetails = team_details(id)
    players = get_pitchers(id)
    return render(request, "team_pitchers.html", { "id":id, "team":teamdetails,"players":players })

def player(request, id=id):
    return render(request, "player_pitchers.html", { "id":id })