class Player:
    def __init__(self, data):
        self.name = data['name']
        self.team = data['team']
        self.nationality = data['nationality']
        self.goals = data['goals']
        self.assists = data['assists']
    
    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"
