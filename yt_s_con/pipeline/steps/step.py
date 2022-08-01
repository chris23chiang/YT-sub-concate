from abc import ABC
from abc import abstractmethod


class Step(ABC):  # 繼承ABC就變成一個抽象類別
    def __init__(self):
        pass

    @abstractmethod  # 至少要有一個abstract method
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):  # 繼承python內建的Exception class
    pass
