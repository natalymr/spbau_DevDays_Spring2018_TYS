from PyQt5.QtWidgets import QFrame


class Design:
    RIGHT_COLOR = 'rgb(77, 255, 77)'
    WRONG_COLOR = 'rgb(255, 26, 26)'
    # DEFAULT_COLOR = 'rgb(255, 255, 230)'
    DEFAULT_COLOR = 'rgb(255, 255, 255)'
    DEFAULT_STYLE = 'background-color: {};color: rgb(0,0,0)'.format(DEFAULT_COLOR)
    RIGHT_STYLE = 'background-color: {};color: rgb(0,0,0)'.format(RIGHT_COLOR)
    WRONG_STYLE = 'background-color: {};color: rgb(0,0,0)'.format(WRONG_COLOR)


CHAT_TASKS = 'src/tasks/json/chat_problems/chat_tasks.json'
DICT_WITH_ASYMPTOTICS = 'src/tasks/html/asym/asym_dict.json'

DEFAULT_TEXT = 'Hello, my little friend. Let\'s check your skills!'

INTERVIEWER = 'src/images/interviewer_{}.png'

glob_dict_name = {'n': 'n', 'nlog(n)': 'nlog_n_', 'n^2': 'n^2', 'log(n)': 'log_n_', 'v+e': 'v+e', 've': 've',
                      'elog(e)': 'elog_e_', 'n / log(n)': 'n/log_n_', 'v^2+e': 'v^2+e', '(v+e)log(v)': '_v+e_log_v_',
                      'log(v)': 'log_v_', 'vlog(v)': 'vlog_v_', 'n^(1/2)': 'n^_1/2_', 'const': 'const',
                      'v^2e^2': 'v^2e^2',
                      'mn': 'mn', 'log(mn)': 'log_mn_', 'n^2m^2': 'n^2m^2', 'n / m': 'n/m', 'n^2log(n)': 'n^2log_n_',
                      'nlog(n)log(n)': 'nlog_n_log_n_', 'n^3': 'n^3', 'nlog(log(n))': 'nlog_log_n__'}


def set_style(window):
    window.setFrameShape(QFrame.StyledPanel)
    window.setLineWidth(2)
    window.setFrameShape(QFrame.Box)
    window.setFrameShadow(QFrame.Plain)