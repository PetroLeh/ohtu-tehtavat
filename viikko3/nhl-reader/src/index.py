import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
        )

        players.append(player)

    print("Players from Finland:")

    for player in filter(lambda player: player.nationality == "FIN",
                         sorted(players, key=lambda player: (player.goals + player.assists),
                         reverse=True)):
        print(player)

if __name__ == "__main__":
    main()

