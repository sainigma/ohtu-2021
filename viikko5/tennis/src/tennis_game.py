class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score = self.score + 1

    def __gt__(self, other):
        if self.score < other.score:
            return True
        return False

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [Player(player1_name),Player(player2_name)]

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def won_point(self, player_name):
        self.get_player(player_name).add_point()

    def final_battle(self):
        if not (self.players[0].score >= 4 or self.players[1].score >= 4):
            return False

        delta_score = abs(self.players[0].score - self.players[1].score)
        if delta_score == 0:
            return 'Deuce'
        
        sorted_players = sorted(self.players)
        label = 'Advantage' if delta_score < 2 else "Win for"
        return f'{label} {sorted_players[0].name}'

    def normal_score(self):
        labels = ["Love", "Fifteen", "Thirty", "Forty"]
        player_labels = list(map(lambda player: labels[player.score], self.players))
        if player_labels[0] == player_labels[1]:
            return f'{player_labels[0]}-All'
        return f'{player_labels[0]}-{player_labels[1]}'

    def get_score(self):
        final_battle = self.final_battle()
        if final_battle:
            return final_battle

        return self.normal_score()
