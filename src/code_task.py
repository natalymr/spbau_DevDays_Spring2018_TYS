from enum import Enum
import json


class CodeTask:

    def __init__(self, id, difficulty):
        self.difficulty = difficulty
        self.id = id
