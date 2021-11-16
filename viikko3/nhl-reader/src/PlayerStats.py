class PlayerStats:
  def __init__(self, reader):
    self.reader = reader

  def players_by_nationality(self, nation):
    return filter(lambda player: player.nationality == nation, self.reader.get())

  def top_scorers_by_nationality(self, nation):
    return sorted(self.players_by_nationality(nation), reverse = True)