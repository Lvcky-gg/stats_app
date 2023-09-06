from django.shortcuts import render
####################################MOVE TO UTILS
import requests
from html.parser import HTMLParser



################################################################################
def create_teams():
    teams = requests.get("https://statsapi.mlb.com/api/v1/teams?sportId=1")
    Standings = requests.get("https://statsapi.mlb.com/api/v1/standings?leagueId=103,104").json()["records"]

    # print(teams.json()["teams"][0]["division"])
    alEast = [[i["id"], i["name"], i["link"], i["league"]] for i in teams.json()["teams"] if i["division"]["name"] == "American League East"]
    nlEast = [[i["id"], i["name"], i["link"]] for i in teams.json()["teams"] if i["division"]["name"] == "National League East"]
    alCentral = [[i["id"], i["name"], i["link"]] for i in teams.json()["teams"] if i["division"]["name"] == "American League Central"]
    nlCentral = [[i["id"], i["name"], i["link"]] for i in teams.json()["teams"] if i["division"]["name"] == "National League Central"]
    alWest = [[i["id"], i["name"], i["link"]] for i in teams.json()["teams"] if i["division"]["name"] == "American League West"]
    nlWest = [[i["id"], i["name"], i["link"]] for i in teams.json()["teams"] if i["division"]["name"] == "National League West"]
    alEastNames = [i[1] for i in alEast]
    nlEastNames = [i[1] for i in nlEast]
    alCentralNames = [i[1] for i in alCentral]
    nlCentralNames = [i[1] for i in nlCentral]
    alWestNames = [i[1] for i in alWest]
    nlWestNames = [i[1] for i in nlWest]
    ale = []
    nle = []
    alc = []
    nlc = []
    alw = []
    nlw = []
    for i in range(len(Standings)):
        teamStanding = Standings[i]['teamRecords']
# https://www.mlbstatic.com/team-logos/141.svg
        for k in range(len(teamStanding)):
            team = {"team":teamStanding[k]['team'],"leagueRecord":teamStanding[k]['leagueRecord'], "l10Record":teamStanding[k]['records']['splitRecords'][8], "diff":teamStanding[k]['runDifferential'], "gb":teamStanding[k]["gamesBack"]}
            if teamStanding[k]['team']['name'] in alEastNames:
                ale.append(team)
            elif teamStanding[k]['team']['name'] in nlEastNames:
                nle.append(team)
            elif teamStanding[k]['team']['name'] in alCentralNames:
                alc.append(team)
            elif teamStanding[k]['team']['name'] in nlCentralNames:
                nlc.append(team)
            elif teamStanding[k]['team']['name'] in alWestNames:
                alw.append(team)
            elif teamStanding[k]['team']['name'] in nlWestNames:
                nlw.append(team)
    return [{"name":"AL East","div":ale},
                {"name":"NL East","div":nle},
                {"name":"AL Central","div":alc},
                {"name":"NL Central","div":nlc},
                {"name":"AL West","div":alw},
                {"name":"NL West","div":nlw}]
    

def parseHTML(val):
    news_list = []
    url = requests.get(val).text
    xmlItems = url.split('<item>')[1::][1::]
    for i in range(0,5):
        desc = xmlItems[i].split('<title>' )[1].split('</title>')[0].split('<![CDATA[')[1].split(']]>')[0]
        link = xmlItems[i].split('<link>' )[1].split('</link>')[0]
        image = xmlItems[i].split('href="' )[1].split('"/>')[0]
        date = xmlItems[i].split('<pubDate>')[1].split('</pubDate>')[0].split(', ')[1].split(' ')
        author = xmlItems[i].split('<dc:creator>' )[1].split('</dc:creator>')[0]
        month = date[1]
        day = date[0]
        year = date[2]
        # print(xmlItems[i])
        news_list.append({"title":desc, 
                          "link":link, 
                          "image":image, 
                          "date":date, 
                          "author":author, 
                          "day":day,
                          "month":month,
                          "year":year,
                          })
    return  news_list
# POLYAS
# Need a list of each team in a division
# need a List each containing the following: Name of Team, Team ID, Team Link, win, loss, pct, GB, L10, DIFF

def home(response):
    news = parseHTML("https://www.mlb.com/feeds/news/rss.xml")
    divisions = create_teams() 
    return render(response, "home.html", 
                  {'divisions':divisions, 
                    "news":news})

    
    