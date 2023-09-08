import requests


def get_pitchers(id):
    players = []
    val = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}/roster/Active?hydrate=person(stats(type=season))").json()["roster"]
    for i in range(len(val)):
        
        if val[i]["position"]["abbreviation"] == "P":
            
            value = {
                "id":val[i]["person"]["id"],
                "position":val[i]["position"]["abbreviation"],
                "fullname":val[i]["person"]["fullName"],
                "jerseyNumber":val[i]["jerseyNumber"],
                "name":val[i]["person"]["fullName"],
                "age":val[i]["person"]["currentAge"],
                "height":val[i]["person"]["height"],
                "weight":val[i]["person"]["weight"],
                "b":val[i]["person"]["batSide"]["code"],
                "t":val[i]["person"]["pitchHand"]["code"],
                "IP":val[i]["person"]["stats"][0]["splits"][0]["stat"]["inningsPitched"],
                "ERA":val[i]["person"]["stats"][0]["splits"][0]["stat"]["era"],
                "SO":val[i]["person"]["stats"][0]["splits"][0]["stat"]["strikeOuts"],
                "WHIP":val[i]["person"]["stats"][0]["splits"][0]["stat"]["whip"],
                "BB":val[i]["person"]["stats"][0]["splits"][0]["stat"]["baseOnBalls"],
                "HR9":val[i]["person"]["stats"][0]["splits"][0]["stat"]["homeRunsPer9"],
                "OPS":val[i]["person"]["stats"][0]["splits"][0]["stat"]["ops"],
            }
    
        
            players.append(value)
    return players