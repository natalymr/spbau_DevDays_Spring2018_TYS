

class Design:
    RIGHT_COLOR = 'rgb(77, 255, 77)'
    WRONG_COLOR = 'rgb(255, 26, 26)'
    # DEFAULT_COLOR = 'rgb(255, 255, 230)'
    DEFAULT_COLOR = 'rgb(255, 255, 255)'
    DEFAULT_STYLE = 'background-color: {};color: rgb(0,0,0)'.format(DEFAULT_COLOR)
    RIGHT_STYLE = 'background-color: {};color: rgb(0,0,0)'.format(RIGHT_COLOR)
    WRONG_STYLE = 'background-color: {};color: rgb(0,0,0)'.format(WRONG_COLOR)


CHAT_TASKS = {1: 'src/tasks/chat_tasks_1.json'} #,
              # 2: 'src/tasks/chat_tasks_2.json',
              # 3: 'src/tasks/chat_tasks_3.json'}

DEFAULT_TEXT = 'Hello, my little friend. Let\'s check your skills!'

INTERVIEWER = 'src/images/interviewer_{}.png'
