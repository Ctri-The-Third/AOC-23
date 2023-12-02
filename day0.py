from abc import ABC, abstractmethod
import regex as re


class Challenge:
    @abstractmethod
    def solve_part_1(self, input_date) -> str:
        pass

    @abstractmethod
    def solve_part_2(self, input_date) -> str:
        pass
