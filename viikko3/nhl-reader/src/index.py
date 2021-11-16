import requests
from datetime import datetime
from player import Player

def printPlayersByNation(players, nation):
    print(f"Players from {nation} {datetime.now()}\n")

    playerList = filter(lambda player: player.nationality == nation, players)

    playerList = sorted(playerList, reverse = True)

    for player in playerList:
        print(player)

def main():
    url = 'https://nhlstatisticsforohtu.herokuapp.com/players'
    response = requests.get(url).json()

    players = []
    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    printPlayersByNation(players, 'FIN')    

if __name__ == "__main__":
    main()
