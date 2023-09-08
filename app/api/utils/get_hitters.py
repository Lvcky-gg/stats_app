import requests


def get_hitters(id):
    players = []
    val = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}/roster/Active?hydrate=person(stats(type=season))").json()["roster"]
    for i in range(len(val)):
        
        if val[i]["position"]["abbreviation"] != "P":
            pa = 0
            h = 0
            doubles = 0
            triples = 0
            hr = 0
            sb = 0
            avg = 0
            obp = 0
            ops = 0
            
            if 'stats' in val[i]["person"]:
                stats = val[i]["person"]["stats"][0]["splits"][0]["stat"]
                if 'plateAppearances' in stats:
                    pa = stats["plateAppearances"]
                if 'hits' in stats:
                    h = stats["hits"]
                if 'doubles' in stats:
                    doubles = stats["doubles"]
                if 'triples' in stats:
                    triples = stats["triples"]
                if 'homeRuns' in stats:
                    hr = stats["homeRuns"]
                if 'stolenBases' in stats:
                    sb = stats["stolenBases"]
                if 'avg' in stats:
                    avg = stats["avg"]
                if 'obp' in stats:
                    obp = stats["obp"]
                if 'ops' in stats:
                    ops = stats["ops"]
            
            value = {
                "id":val[i]["person"]["id"],
                "position":val[i]["position"]["abbreviation"],
                "fullname":val[i]["person"]["fullName"],
                "jerseyNumber":val[i]["jerseyNumber"],
                "name":val[i]["person"]["fullName"],
                "age":val[i]["person"]["currentAge"],
                "height":val[i]["person"]["height"],
                "weight":val[i]["person"]["weight"],
                "birthDate":val[i]["person"]["birthDate"],
                "b":val[i]["person"]["batSide"]["code"],
                "t":val[i]["person"]["pitchHand"]["code"],
                "pa":pa,
                "h":h,
                "2b":doubles,
                "3b":triples,
                "hr":hr,
                "sb":sb,
                "avg":avg,
                "obp":obp,
                "ops":ops,
            }
    
        
            players.append(value)
    return players