import requests


def get_pitchers(id):
    players = []
    val = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{id}/roster/Active?hydrate=person(stats(type=season))").json()["roster"]
    print(val)
    for i in range(len(val)):
        stats = {}
        era = 0.00
        ip = 0
        so = 0
        bb = 0
        hr9 = 0
        ops = 0
        if val[i]["position"]["abbreviation"] == "P":
            if 'stats' in val[i]["person"]:
                stats = val[i]["person"]["stats"][0]["splits"][0]["stat"]
                if 'inningsPitched' in stats:
                    ip = stats["inningsPitched"]
                if 'era' in stats:
                    era = stats["era"]
                if 'strikeOuts' in stats:
                    so = stats["strikeOuts"]
                if 'whip' in stats:
                    whip = stats["whip"]
                if 'baseOnBalls' in stats:
                    bb = stats["baseOnBalls"]
                if 'homeRunsPer9' in stats:
                    hr9 = stats["homeRunsPer9"]
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
                "b":val[i]["person"]["batSide"]["code"],
                "t":val[i]["person"]["pitchHand"]["code"],
                "IP":ip,
                "ERA":era,
                "SO":so,
                "WHIP":whip,
                "BB":bb,
                "HR9":hr9,
                "OPS":ops,
            }
    

            players.append(value)
    return players