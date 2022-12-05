import random
import string
from os.path import exists as file_exists
import os
from test import create_dir


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear_folder():
    arr = os.listdir()
    not_touch = ["checker.py", "a.py", "test.py"]
    for i in arr:
        if not i in not_touch:
            print(i)
            os.remove(i)


def approve_existing(file_name):
    if file_exists(file_name):
        return True
    else:
        return False


def name_generator(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def character_generator(length):
    letters = string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# SETTINGS
tests_counter = 1000
success_counter = 0
failed_counter = 0
fail_error = []

print(bcolors.HEADER + "# START TEST 1 ..." + bcolors.ENDC)
# ------------------------ Func 1 ------------------------
print("## START LITERAL ...")
dir_name = []
for x in range(tests_counter):
    o = "| Func[1][NORMAL] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    dir_name.append(name_generator(8))
    create_dir(dir_name[x])
    if not approve_existing(dir_name[x]):
        message = o + "Not found dir: " + dir_name[x]
        fail_error.append(bcolors.FAIL + " " + message + bcolors.ENDC)
        failed_counter = failed_counter + 1
    else:
        success_counter = success_counter + 1
print("# START CLEANING AFTER TEST 1 ...")
for x in dir_name:
    if os.path.exists(x):
        os.rmdir(x)
dir_name = []
print("## DONE LITERAL")

print("## START NUMERIC ...")
for x in range(tests_counter):
    o = "| Func[1][NUMERIC] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    dir_name.append(str(random.randrange(10000000, 999999999, 1)))
    create_dir(dir_name[x])
    if not approve_existing(dir_name[x]):
        fail_error.append(bcolors.FAIL + " " + o + "Not found dir: " + dir_name[x] + bcolors.ENDC)
        failed_counter = failed_counter + 1
    else:
        success_counter = success_counter + 1
print("# START CLEANING AFTER TEST 2 ...")
for x in dir_name:
    if os.path.exists(x):
        os.rmdir(x)
dir_name = []
print("## DONE NUMERIC")

print("")
print("")
print("########### Result ###########")
print("Success: " + bcolors.OKGREEN + str(success_counter) + bcolors.ENDC)
print("Failed: " + bcolors.FAIL + str(failed_counter) + bcolors.ENDC)
if failed_counter > 0:
    for x in fail_error:
        print(x)
    print(bcolors.FAIL + "you need to do better" + bcolors.ENDC)
else:
    print(bcolors.OKGREEN + "Congratulations :)" + bcolors.ENDC)
