import requests


def get_hitters(id):
    players = []
    val = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}/roster/Active?hydrate=person(stats(type=season))").json()["roster"]
    for i in range(len(val)):
        
        if val[i]["position"]["abbreviation"] != "P":
            
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
                "pa":val[i]["person"]["stats"][0]["splits"][0]["stat"]["plateAppearances"],
                "h":val[i]["person"]["stats"][0]["splits"][0]["stat"]["hits"],
                "2b":val[i]["person"]["stats"][0]["splits"][0]["stat"]["doubles"],
                "3b":val[i]["person"]["stats"][0]["splits"][0]["stat"]["triples"],
                "hr":val[i]["person"]["stats"][0]["splits"][0]["stat"]["homeRuns"],
                "sb":val[i]["person"]["stats"][0]["splits"][0]["stat"]["stolenBases"],
                "avg":val[i]["person"]["stats"][0]["splits"][0]["stat"]["avg"],
                "obp":val[i]["person"]["stats"][0]["splits"][0]["stat"]["obp"],
                "ops":val[i]["person"]["stats"][0]["splits"][0]["stat"]["ops"],
            }
    
        
            players.append(value)
    return players