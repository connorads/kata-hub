import pytest

from yam import calculate_possible_scores


@pytest.mark.parametrize("input,expected", [
    ((1, 1, 1, 1, 1),
     {'Aces': 5, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a kind': 5,
      'Four of a kind': 5, 'Full house': 0, 'Small straight': 0, 'Large straight': 0, 'Chance': 5, 'Yams': 50}),
    ((1, 2, 3, 4, 5),
     {'Aces': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 0, 'Three of a kind': 0,
      'Four of a kind': 0, 'Full house': 0, 'Small straight': 30, 'Large straight': 40, 'Chance': 15, 'Yams': 0}),
    ((1, 1, 1, 2, 2),
     {'Aces': 3, 'Twos': 4, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a kind': 7,
      'Four of a kind': 0, 'Full house': 25, 'Small straight': 0, 'Large straight': 0, 'Chance': 7, 'Yams': 0}),
    ((1, 2, 3, 4, 6),
     {'Aces': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 0, 'Sixes': 6, 'Three of a kind': 0,
      'Four of a kind': 0, 'Full house': 0, 'Small straight': 30, 'Large straight': 0, 'Chance': 16, 'Yams': 0}),
    ((6, 6, 6, 6, 1),
     {'Aces': 1, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 24, 'Three of a kind': 25,
      'Four of a kind': 25, 'Full house': 0, 'Small straight': 0, 'Large straight': 0, 'Chance': 25, 'Yams': 0}),
])
def test_calculate_possible_scores(input, expected):
    assert calculate_possible_scores(input) == expected
