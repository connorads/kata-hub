from typing import Literal

UpperSection = Literal['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
LowerSection = Literal['Three of a kind', 'Four of a kind',
                       'Full house', 'Small straight', 'Large straight', 'Chance', 'Yams']
Category = Literal[UpperSection, LowerSection]
PossibleScores = dict[Category, int]
Dice = Literal[1, 2, 3, 4, 5, 6]
Roll = tuple[Dice, Dice, Dice, Dice, Dice]


def calculate_possible_scores(roll: Roll) -> PossibleScores:
    return {
        'Aces': sum(dice for dice in roll if dice == 1),
        'Twos': sum(dice for dice in roll if dice == 2),
        'Threes': sum(dice for dice in roll if dice == 3),
        'Fours': sum(dice for dice in roll if dice == 4),
        'Fives': sum(dice for dice in roll if dice == 5),
        'Sixes': sum(dice for dice in roll if dice == 6),
        'Three of a kind': sum(roll) if any(roll.count(dice) >= 3 for dice in roll) else 0,
        'Four of a kind': sum(roll) if any(roll.count(dice) >= 4 for dice in roll) else 0,
        'Full house': 25 if any(roll.count(dice) == 3 for dice in roll) and any(roll.count(dice) == 2 for dice in roll) else 0,
        'Small straight': 30 if all(roll.count(dice) >= 1 for dice in [1, 2, 3, 4]) or all(roll.count(dice) >= 1 for dice in [2, 3, 4, 5]) or all(roll.count(dice) >= 1 for dice in [3, 4, 5, 6]) else 0,
        'Large straight': 40 if all(roll.count(dice) == 1 for dice in [1, 2, 3, 4, 5]) or all(roll.count(dice) == 1 for dice in [2, 3, 4, 5, 6]) else 0,
        'Chance': sum(roll),
        'Yams': 50 if any(roll.count(dice) == 5 for dice in roll) else 0
    }
