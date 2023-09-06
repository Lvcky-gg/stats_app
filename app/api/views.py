from django.shortcuts import render

from .utils.fetch_teams import create_teams
from .utils.fetch_news import parseHTML




def home(response):
    news = parseHTML("https://www.mlb.com/feeds/news/rss.xml")
    divisions = create_teams() 
    return render(response, "home.html", 
                  {'divisions':divisions, 
                    "news":news})

    
def team_hitters(request, id=id):
    return render(request, "team_hitters.html", {})  