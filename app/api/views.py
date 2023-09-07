from django.shortcuts import render
import requests

from .utils.fetch_teams import create_teams
from .utils.fetch_news import parseHTML
from .utils.team_details import team_details




def home(response):
    news = parseHTML("https://www.mlb.com/feeds/news/rss.xml")
    divisions = create_teams() 
    return render(response, "home.html", 
                  {'divisions':divisions, 
                    "news":news})

    
def team_hitters(request, id=id):
    teamdetails = team_details(id)
    players = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}/roster").json()["roster"]
    
    
        
    
    return render(request, "team_hitters.html", { "id":id, "team":teamdetails, "players":players }) 