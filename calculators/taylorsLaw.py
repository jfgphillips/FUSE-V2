def taylors_law(expected_reserves, days_per_year):
    """
    :param expected_reserves: proven + probable reserves of a mine (tonnes)
    :param days_per_year: mine operation days in a year (d/yr)
    :return: a value in tonnes per day for most economical mining rates
    """
    numerator = expected_reserves ** (3 / 4)
    mining_rate = 5 * (numerator / days_per_year)
    return mining_rate
