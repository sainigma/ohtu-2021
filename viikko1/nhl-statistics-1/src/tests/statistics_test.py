import unittest
from statistics import Statistics
from player import Player

players = [
      Player("Semenko", "EDM", 4, 12),
      Player("Lemieux", "PIT", 45, 54),
      Player("Kurri",   "EDM", 37, 53),
      Player("Yzerman", "DET", 42, 56),
      Player("Gretzky", "EDM", 35, 89),
    ]

class PlayerReaderDummy:
  def get_players(self):
    return players

class TestStatistics(unittest.TestCase):
  def setUp(self):
    self.stats = Statistics(PlayerReaderDummy())

  def test_top_scorer_correct_size(self):
    length = len(self.stats.top_scorers(5))
    self.assertAlmostEqual(len(players), length)
  
  def test_top_scorer_correct_size_when_greater_than_db_size(self):
    length = len(self.stats.top_scorers(100))
    self.assertAlmostEqual(len(players), length)
  
  def test_top_scorer_nan_input(self):
    length = len(self.stats.top_scorers(-1))
    self.assertAlmostEqual(0, length)

  def test_search_existing_player(self):
    target = players[0].name
    result = self.stats.search(target)
    self.assertEqual(result.name, target)

  def test_search_nonexisting_player(self):
    self.assertEqual(self.stats.search("Kummitus"), None)

  def team_search(self, tag):
    teamSize = 0
    for player in players:
      if player.team == tag:
        teamSize = teamSize + 1
    result = self.stats.team(tag)
    self.assertEqual(teamSize, len(result))
    return result

  def test_team_search(self):
    teams = ["EDM", "PIT", "DET"]
    for team in teams:
      self.team_search(team)

  def test_team_search_nonexisting(self):
    result = self.team_search("NUL")
    self.assertEqual(result, [])