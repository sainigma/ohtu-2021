import requests
from datetime import datetime
from player import Player

def printPlayersFromNation(players, nation):
    print(f"Players from {nation} {datetime.now()}\n")
    for player in players:
        if player.nationality == nation:
            print(player)

def main():
    url = 'https://nhlstatisticsforohtu.herokuapp.com/players'
    response = requests.get(url).json()

    players = []
    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    printPlayersFromNation(players, 'FIN')

if __name__ == "__main__":
    main()
