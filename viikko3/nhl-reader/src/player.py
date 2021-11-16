class Player:
    def __init__(self, data):
        self.name = data['name']
        self.team = data['team']
        self.nationality = data['nationality']
        self.goals = data['goals']
        self.assists = data['assists']
    
    def __str__(self):
        goals = str(self.goals)
        assists = str(self.assists)
        total = str(self.goals + self.assists)
        return f"{self.name:20} {self.team} {goals:2} + {assists:2} = {total:2}"

    def __lt__(self, other):
        if other.goals + other.assists > self.goals + self.assists:
            return True
        return False