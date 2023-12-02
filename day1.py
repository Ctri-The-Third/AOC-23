import regex as re
from day0 import Challenge


class Day1(Challenge):
    def solve_part_1(self, input_data: list[str]) -> str:
        all_numbers = re.compile(r"([0-9])")
        total_value = 0
        for line in input_data:
            try:
                numbers = all_numbers.findall(line)

                first_number = int(f"{numbers[0]}{numbers[-1]}")
                print(f"{first_number} - {line}".strip())
                total_value += first_number
            except Exception as e:
                pass

        return total_value

    def solve_part_2(self, input_data: list[str]) -> str:
        print("--- Part Two ---")
        all_numbers = re.compile(
            r"([0-9]|one|two|three|four|five|six|seven|eight|nine)"
        )
        values = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        total_value = 0
        for line in input_data:
            try:
                numbers = all_numbers.findall(line, overlapped=True)
                first_number = values.get(numbers[0], numbers[0])
                last_number = values.get(numbers[-1], numbers[-1])
                final_number = int(f"{first_number}{last_number}")
                print(f"{first_number}{last_number} - {line}".strip())
                total_value += final_number
            except Exception as e:
                pass

        return total_value


if __name__ == "__main__":
    challenge = Day1()

    challenge_text = open("challenge_texts/day1.txt").readlines()
    print(challenge.solve_part_1(challenge_text))
    print(challenge.solve_part_2(challenge_text))
