from matchers import HasAtLeast, HasFewerThan, PlaysIn, Not, Or

class QueryBuilder:
  def __init__(self, matchers=[[]]):
    self._matchers = matchers

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

  def oneOf(self, query1, query2):
    self._matchers[0] = query1._matchers[0]
    if len(self._matchers) < 2:
      self._matchers.append([])
    self._matchers[1] = query2._matchers[0]
    return self

  def build(self):
    query = QueryBuilder(self._matchers)
    self._matchers = [[]]
    return query

  def playsIn(self, team):
    self._matchers[0].append(PlaysIn(team))
    return self

  def hasAtLeast(self, value, attr):
    self._matchers[0].append(HasAtLeast(value, attr))
    return self
  
  def hasFewerThan(self, value, attr):
    self._matchers[0].append(HasFewerThan(value, attr))
    return self