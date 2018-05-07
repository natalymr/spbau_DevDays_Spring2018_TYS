from subprocess import call
from subprocess import check_output
import re
import json


def mv_zips_from_downloads(required_dir = None):
    """
    This function move all zips from Downloads to cur dir.
    """
    pwd = check_output("pwd", shell=True)
    if required_dir is None:
        required_dir = tmp1 = "".join(map(chr, pwd))

    bash_command = "mv ~/Downloads/*linux.zip " + required_dir
    call(bash_command, shell=True)


cod_problems_difficulty = {'abacus-6': 3, 'bfs-5': 2, 'connected-components-1': 2, 'connected-graph-2': 2,
                           'dominoes-25': 5, 'fibonacci-sequence-1': 5, 'houses-4': 2, 'kindergarden-3': 2,
                           'large-array-12': 3, 'lost-streets-13': 5, 'missing-battleship-5': 2,
                           'movie-5': 3, 'palindrom-5': 2, 'segment-tree-min-max-3': 3,
                           'shmoogle-3': 2, 'subway-5': 3}



def unzip_each_problem(required_dir = None):
    """
    This function
    :param required_dir: name of dir from which all zips are taken
    :return: list with names of all problems
    """
    # находим все файлы, в необходимой директории
    if required_dir is not None:
        ls_command = "ls " + required_dir
    else:
        ls_command = "ls"
    ls = check_output(ls_command, shell=True)
    tmp1 = "".join(map(chr, ls))
    list_of_all_files = tmp1.split('\n')

    # находим имена всех zip файлов
    list_of_files_to_unzip = []
    for i in range(len(list_of_all_files)):
        result = re.split(r'.zip', list_of_all_files[i])
        if len(result) > 1:
            list_of_files_to_unzip.append(result[0])

    # распаковываем каждый архив и помещаем все файлы в директорию с соответствующим именем
    for i in range(len(list_of_files_to_unzip)):
        # создаем необходимую папку
        dir_name = list_of_files_to_unzip[i][:-6]
        mkdir_command = "mkdir " + dir_name
        call(mkdir_command, shell=True)

        if required_dir is not None:
            path_to_zip_with_its_name = required_dir + "/" + dir_name
        else:
            path_to_zip_with_its_name = dir_name

        unzip_command = "unzip " + path_to_zip_with_its_name + "\$linux.zip " + "-d " + dir_name
        call(unzip_command, shell=True)

    result = []
    for i in range(len(list_of_files_to_unzip)):
        result.append(list_of_files_to_unzip[i][:-6])

    return result


def take_json_file_for_each_command(list_with_names_of_all_problems = None,
                                    path_to_dirs_with_problems = None,
                                    required_dir = None):
    """
    This function take usual json file of a problem and take all test: [input, output] and add to this json file.
    :param list_with_names_of_all_problems:
    :param path_to_dirs_with_problems: path where all dirs with problems are. If its None path = pwd
    :param required_dir: where all result will be saved. If its None path = pwd
    :return:
    """
    if path_to_dirs_with_problems is None:
        path_to_dirs_with_problems = ""

    if required_dir is None:
        required_dir = ""

    if list_with_names_of_all_problems is None:
        global list_of_problems_name
        list_with_names_of_all_problems = list_of_problems_name

    # take all test for each problem and save to test.json
    if required_dir == "":
        path_to_tests_json = required_dir + "tests_for_all_problems.json"
    else:
        path_to_tests_json = required_dir + "/tests_for_all_problems.json"

    touch_command1 = "touch " + path_to_tests_json
    call(touch_command1, shell=True)

    for_all_problems = []
    for cur_problem in list_with_names_of_all_problems:
        cur_problem_d = {}
        cur_problem_d["problem_name_t"] = cur_problem
        path_to_tests = path_to_dirs_with_problems + cur_problem + "/tests"
        ls_com = "ls " + path_to_tests
        ls_res = check_output(ls_com, shell=True)
        tmp1 = "".join(map(chr, ls_res))
        list_of_all_tests_for_cur_problem = tmp1.split('\n')
        list_of_all_tests_for_cur_problem = list_of_all_tests_for_cur_problem[:-1]
        list_of_all_tests_for_cur_problem.sort()

        if len(list_of_all_tests_for_cur_problem) > 8:
            list_of_all_tests_for_cur_problem = list_of_all_tests_for_cur_problem[:8]

        cur_problems_all_tests = []
        for cur_test in range(0, len(list_of_all_tests_for_cur_problem), 2):
            cur_test_name = list_of_all_tests_for_cur_problem[cur_test]
            cur_test_dict = {}

            with open(path_to_tests + "/" + cur_test_name, "r") as file_r:
                cur_test_dict["input"] = file_r.readlines()

            with open(path_to_tests + "/" + cur_test_name + ".a", "r") as file_r:
                cur_test_dict["output"] = file_r.readlines()

            cur_problems_all_tests.append(cur_test_dict)
        cur_problem_d["tests"] = cur_problems_all_tests

        for_all_problems.append(cur_problem_d)

    with open(path_to_tests_json, "a") as file_json_w:
        json.dump(for_all_problems, file_json_w, indent=4)

    if required_dir == "":
        path_to_problems_json = required_dir + "coding_problems.json"
    else:
        path_to_problems_json = required_dir + "/coding_problems.json"

    touch_command2 = "touch " + path_to_problems_json
    call(touch_command2, shell=True)

    iter = 0
    all_problem_in_json_list = []
    for cur_problem in list_with_names_of_all_problems:
        iter += 1
        ls_com1 = check_output("ls " + path_to_dirs_with_problems + cur_problem + "/statements/", shell=True)
        tmp1 = tmp1 = "".join(map(chr, ls_com1))
        list_of_all_files = tmp1.split('\n')

        path_to_json = path_to_dirs_with_problems + cur_problem + \
                       "/statements/" + list_of_all_files[0] + "/problem-properties.json"
        problems_key = ["legend", "input", "output", "sampleTests", "name"]

        problem = {}
        problem["id"] = iter
        problem["problem_name_t"] = cur_problem
        problem["difficulty"] = cod_problems_difficulty[cur_problem]
        with open(path_to_json, "r") as file_r:
            text = json.load(file_r)
            for key in problems_key:
                problem[key] = text[key]
        all_problem_in_json_list.append(problem)

    print("BEFORE")
    with open(path_to_problems_json, "a") as file_w:
        json.dump(all_problem_in_json_list, file_w, indent=4)
    print("AFTER")

#mv_zips_from_downloads()
#list_problems_name = []
#list_problems_name = unzip_each_problem()

#ls1 = check_output("ls sources/tmp", shell=True)
#tmp1 = "".join(map(chr, ls1))
#list_of_problems_name = tmp1.split('\n')
#list_of_problems_name = list_of_problems_name[:-1]

#test_cod_pr_d_dict()


#take_json_file_for_each_command(list_of_problems_name, "sources/tmp/", "sources")


