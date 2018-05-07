from enum import Enum
import json


class TaskType:
    TEST = 1
    YES_NO = 2
    SINGLE_ANSWER = 3


class Difficulties:
    EASY = 1
    MEDIUM = 2
    HARD = 3


class ChatTask:

    def __init__(self, json_dict, difficulty, id=None):
        self.difficulty = difficulty
        if id is None:
            self.id = json_dict.get('id', -1)
            self.type = json_dict.get('type', None)
            self.right_answers = json_dict.get('right_answer', [])
            self.proposed_answers = json_dict.get('proposed_answer', [])
            self.legend = json_dict.get('legend', '')
        else:
            self.id = id


class CodeTask:

    def __init__(self, id, difficulty):
        self.difficulty = difficulty
        self.id = id
