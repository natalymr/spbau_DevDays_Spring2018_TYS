from enum import Enum
import json


class TaskType(Enum):
    TEST = 1
    YES_NO = 2
    # CODING = 2
    SINGLE_ANSWER = 3

class Difficulties(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class ChatTask:

    def __init__(self, json_dict, difficulty):
        self.id = json_dict.get('id', -1)
        self.type = json_dict.get('type', None)
        self.difficulty = difficulty
        self.date = None
        self.right_answers = json_dict.get('right_answer', [])
        self.proposed_answers = json_dict.get('proposed_answer', [])
        self.legend = json_dict.get('legend', '')