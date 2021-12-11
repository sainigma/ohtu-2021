from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher1 = (
        query.playsIn('PHI')
        .hasAtLeast(10, 'assists')
        .hasFewerThan(5, 'goals')
        .build()
        )
    
    matcher2 = (
        query.playsIn('EDM')
        .hasAtLeast(40, 'points')
        .build()
    )
    
    matcher = query.oneOf(matcher1, matcher2).build()

    '''
    matcher1 = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    matcher2 = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    matcher3 = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )
    '''

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
