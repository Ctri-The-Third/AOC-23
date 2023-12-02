from day0 import Challenge
import re


class day2(Challenge):
    def __init__(self) -> None:
        super().__init__()
        self.pt1_total_cubes = {"red": 12, "green": 13, "blue": 14}

    def solve_part_1(self, input_data: list[str]) -> str:
        valid_games = 0
        pattern = re.compile(r"(([0-9]+) ([a-z]+))")
        for line in input_data:
            game_id = int(line.split(":")[0].split(" ")[1])
            matches = pattern.findall(line)
            for match in matches:
                if self.pt1_total_cubes[match[2]] < int(match[1]):
                    game_id = 0
                    break
            valid_games += game_id
        return valid_games

    def is_game_valid(self, found_cubes: dict) -> bool:
        for cube in found_cubes:
            if found_cubes[cube] > self.pt1_total_cubes[cube]:
                return False
        return True

    def solve_part_2(self, input_data: list[str]) -> str:
        pattern = re.compile(r"(([0-9]+) ([a-z]+))")
        total_power = 0
        for line in input_data:
            found_cubes = {c: 0 for c in self.pt1_total_cubes}
            matches = pattern.findall(line)
            for match in matches:
                found_cubes[match[2]] = max(found_cubes[match[2]], int(match[1]))
            game_power = 1
            for cube_count in found_cubes.values():
                game_power *= cube_count
            total_power += game_power
        return total_power


if __name__ == "__main__":
    challenge = day2()

    result = challenge.solve_part_1(open("challenge_texts/day2.txt").readlines())
    print(f"Part 1: {result}")
    result = challenge.solve_part_2(open("challenge_texts/day2.txt").readlines())
    print(f"Part 2: {result}")
