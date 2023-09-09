import requests

def team_details(id):
    team = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}").json()
    listTeam= team["teams"][0]
    division = listTeam["division"]["name"]
    Standings = requests.get("https://statsapi.mlb.com/api/v1/standings?leagueId=103,104").json()["records"]
    teamstats = []
    
    for i in range(len(Standings)):
        teamStanding = Standings[i]['teamRecords']
        for k in range(len(teamStanding)):
            teamVal = {"team":teamStanding[k]['team'],"leagueRecord":teamStanding[k]['leagueRecord'], 
                    "l10Record":teamStanding[k]['records']['splitRecords'][8], 
                    "diff":teamStanding[k]['runDifferential'], 
                    "gb":teamStanding[k]["gamesBack"],
                    "leagueRank":teamStanding[k]["leagueRank"],
                    "divisionRank":teamStanding[k]["divisionRank"],
                    "division":division,
                    }
            teamstats.append(teamVal)
    
    return [i for i in teamstats if i["team"]["id"] == int(id)][0]
    
    