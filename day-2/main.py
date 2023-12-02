from pipe import map
from itertools import accumulate
from pprint import pprint as print

with open("./input-1.txt") as input_fp:
    input_data = input_fp.read().splitlines()

##############
## PART - 1 ##
##############


BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def is_extraction_possible(bag: dict, extracted_cubes: dict):
    return all(
        count <= BAG[color]
        for color, count in extracted_cubes.items()
    )

def parse_game(line: str):
    game_number = line.split(":")[0].split(" ")[1]
    games = (
        line.split(": ")[1].split("; ")
        | map(lambda x: x.split(", ")) # x = "3 blue, 4 red"
        | map(
            lambda y: dict(
                y
                | map(lambda y: list( # y = [["4 red"], ["2 blue"]]
                    y.split(", ")
                    | map(lambda z: (z.split(" ")[1], int(z.split(" ")[0]))) # z = "4 red"
                ))
                | map(lambda y_split: y_split[0]) # y_split = [("4", "red")]
            )
        )
    )
    return int(game_number), list(games)
     

possible_games = []
for game_line in input_data:
    game_number, extractions = parse_game(game_line)
    is_game_possible = all(
        is_extraction_possible(BAG, extraction)
        for extraction in extractions
    )
    if is_game_possible:
        possible_games.append(game_number)
print(sum(possible_games))


##############
## PART - 2 ##
##############

def get_min_bag(extractions):
    min_bag = {}
    print(extractions)
    for extraction in extractions:
        for color, count in extraction.items():
            if min_bag.get(color) is None or min_bag.get(color) < count:
                min_bag[color] = count
    return min_bag


def multiply(numbers: list):
    acc = 1
    for number in numbers:
        acc *= number
    return acc


powers = []
for game_line in input_data:
    game_number, extractions = parse_game(game_line)
    min_bag = get_min_bag(extractions)
    bag_power = multiply(min_bag.values())
    powers.append(bag_power)

print(sum(powers))
