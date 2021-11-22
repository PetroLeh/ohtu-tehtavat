from playerReader import PlayerReader

class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players = []

        for player in filter(lambda player: player.nationality == nationality,
                         sorted(all_players, key=lambda player: (player.goals + player.assists),
                         reverse=True)):
            players.append(player)
        return players
