
import requests

def create_teams():
    teams = requests.get("https://statsapi.mlb.com/api/v1/teams?sportId=1")
    Standings = requests.get("https://statsapi.mlb.com/api/v1/standings?leagueId=103,104").json()["records"]

    alEast = [[i["id"] ,i["name"], i["link"], i["league"]] for i in teams.json()["teams"] if i["division"]["name"] == "American League East"]
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

        for k in range(len(teamStanding)):
            team = {"team":teamStanding[k]['team'],"leagueRecord":teamStanding[k]['leagueRecord'], 
                    "l10Record":teamStanding[k]['records']['splitRecords'][8], 
                    "diff":teamStanding[k]['runDifferential'], 
                    "gb":teamStanding[k]["gamesBack"],
                    "leagueRank":teamStanding[k]["leagueRank"],
                    "divisionRank":teamStanding[k]["divisionRank"],
                    
                    }
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