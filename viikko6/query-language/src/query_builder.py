from matchers import HasAtLeast, HasFewerThan, PlaysIn, Not, Or

class QueryBuilder:
  def __init__(self):
    self._matchers = [[]]
    self.useAnd = True

  def andMatcher(self, player, matchers):
    for matcher in matchers:
      if not matcher.matches(player):
        return False
    return True

  def matches(self, player):
    for matchers in self._matchers:
      if self.andMatcher(player, matchers):
        return True
    return False

  def build(self):
    return self

  def playsIn(self, team):
    self._matchers[0].append(PlaysIn(team))
    return self

  def hasAtLeast(self, value, attr):
    self._matchers[0].append(HasAtLeast(value, attr))
    return self
  
  def hasFewerThan(self, value, attr):
    self._matchers[0].append(HasFewerThan(value, attr))
    return self