import numbers
import random
import string
import numbers
from os.path import exists as file_exists
import os
from test import create_file
from test import edit_file
from test import delete_file


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
lines_counter = 50
success_counter = 0
failed_counter = 0
fail_error = []

print(bcolors.HEADER + "# START TEST 1 ..." + bcolors.ENDC)
# ------------------------ Func 1 ------------------------
print("## START NORMAL ...")
file_name = []
for x in range(tests_counter):
    o = "| Func[1][NORMAL] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    file_name.append(name_generator(8) + "." + name_generator(4))
    create_file(file_name[x])
    if not approve_existing(file_name[x]):
        message = o + "Not found file: " + file_name[x]
        fail_error.append(bcolors.FAIL + " " + message + bcolors.ENDC)
        failed_counter = failed_counter + 1
    else:
        success_counter = success_counter + 1
print("# START CLEANING AFTER TEST 1:1 ...")
for x in file_name:
    os.remove(x)
file_name = []
print("## DONE 1:1")

print("## START NUMERIC ...")
for x in range(tests_counter):
    o = "| Func[1][NUMERIC] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    file_name.append(str(random.randrange(10000000, 999999999, 1)) + "." + str(random.randrange(1000, 9999, 1)))
    create_file(file_name[x])
    if not approve_existing(file_name[x]):
        fail_error.append(bcolors.FAIL + " " + o + "Not found file: " + file_name[x] + bcolors.ENDC)
        failed_counter = failed_counter + 1
    else:
        success_counter = success_counter + 1
print("# START CLEANING AFTER TEST 1:2 ...")
for x in file_name:
    os.remove(x)
file_name = []
print("## DONE 1:2")

# ------------------------ Func 2 ------------------------

print(bcolors.HEADER + "# START TEST 2 ..." + bcolors.ENDC)
print("## START NORMAL ...")

for x in range(tests_counter):
    file_lines_with_seed_created = []
    o = "| Func[2][NORMAL] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    file_name.append(name_generator(8) + "." + name_generator(4))
    create_file(file_name[x])
    with open(file_name[x], "w") as f_n:
        for a in range(lines_counter):
            seed = name_generator(12) + "\n"
            f_n.write(seed)
            file_lines_with_seed_created.append(seed)
    f_n.close()
    if not approve_existing(file_name[x]):
        message = o + "Not found file: " + file_name[x]
        fail_error.append(bcolors.FAIL + " " + message + bcolors.ENDC)
        failed_counter = failed_counter + 1
        break
    else:
        line_edit = random.randrange(1, lines_counter, 1)
        new_value = name_generator(12) + "\n"
        edit_file(file_name[x], line_edit, new_value)
        f = open(file_name[x], "r")
        lines = f.readlines()
        f.close()
        for lin in range(len(lines)):
            if not lin == line_edit - 1:
                if not lines[lin] == file_lines_with_seed_created[lin]:
                    message = o + "Another line was edited in: " + file_name[x] + " line " + str(lin)
                    fail_error.append(bcolors.FAIL + " " + message + " Expected: " + file_lines_with_seed_created[
                        lin] + " but was: " + lines[lin] + bcolors.ENDC)
                    failed_counter = failed_counter + 1
                else:
                    success_counter = success_counter + 1
            else:
                if not lines[lin] == new_value:
                    message = o + "Another line was edited in: " + file_name[x] + " line " + str(lin)
                    fail_error.append(bcolors.FAIL + " " + message + " Expected: " + new_value + " but was: " +
                                      lines[lin] + bcolors.ENDC)
                    failed_counter = failed_counter + 1
                else:
                    success_counter = success_counter + 1
        os.remove(file_name[x])
print("# START CLEANING AFTER TEST 2:1 ...")
file_name = []
print("## DONE 2:1")

print("## START NUMERIC ...")
for x in range(tests_counter):
    file_lines_with_seed_created = []
    o = "| Func[2][NUMERIC] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    file_name.append(str(random.randrange(1, 12, 1)) + "." + str(random.randrange(1, 12, 1)))
    create_file(file_name[x])
    with open(file_name[x], "w") as f_n:
        for a in range(lines_counter):
            seed = str(random.randrange(1, 12, 1)) + "\n"
            f_n.write(seed)
            file_lines_with_seed_created.append(seed)
    f_n.close()
    if not approve_existing(file_name[x]):
        message = o + "Not found file: " + file_name[x]
        fail_error.append(bcolors.FAIL + " " + message + bcolors.ENDC)
        failed_counter = failed_counter + 1
        break
    else:
        line_edit = random.randrange(1, lines_counter, 1)
        new_value = str(random.randrange(1, 12, 1)) + "\n"
        edit_file(file_name[x], line_edit, new_value)
        f = open(file_name[x], "r")
        lines = f.readlines()
        f.close()
        for lin in range(len(lines)):
            if not lin == line_edit - 1:
                if not lines[lin] == file_lines_with_seed_created[lin]:
                    message = o + "Another line was edited in: " + file_name[x] + " line " + str(lin)
                    fail_error.append(bcolors.FAIL + " " + message + " Expected: " + file_lines_with_seed_created[
                        lin] + " but was: " + lines[lin] + bcolors.ENDC)
                    failed_counter = failed_counter + 1
                else:
                    success_counter = success_counter + 1
            else:
                if not lines[lin] == new_value:
                    message = o + "Another line was edited in: " + file_name[x] + " line " + str(lin)
                    fail_error.append(bcolors.FAIL + " " + message + " Expected: " + new_value +
                                      " but was: " + lines[lin] + bcolors.ENDC)
                    failed_counter = failed_counter + 1
                else:
                    success_counter = success_counter + 1
        os.remove(file_name[x])
print("# START CLEANING AFTER TEST 2:1 ...")
file_name = []
print("## DONE 2:2")

# ------------------------ Func 3 ------------------------

print(bcolors.HEADER + "# START TEST 3 ..." + bcolors.ENDC)
print("## START NORMAL ...")

file_to_delete = []

for x in range(tests_counter):
    o = "| Func[3][NORMAL] test " + str(x + 1) + " for " + str(tests_counter) + " | status: "
    file_name.append(name_generator(8) + "." + name_generator(4))
    create_file(file_name[x])
    if not approve_existing(file_name[x]):
        message = o + "Not created file: " + file_name[x]
        fail_error.append(bcolors.FAIL + " " + message + bcolors.ENDC)
        failed_counter = failed_counter + 1
        break
    else:
        delete_file(file_name[x])
        if approve_existing(file_name[x]):
            message = o + "Found file: " + file_name[x]
            fail_error.append(bcolors.FAIL + " " + message + bcolors.ENDC)
            failed_counter = failed_counter + 1
            file_to_delete.append(file_name[x])
        else:
            success_counter = success_counter + 1

print("# START CLEANING AFTER TEST 2:1 ...")
if len(file_to_delete) > 0:
    for x in file_to_delete:
        os.remove(x)
file_name = []
print("## DONE 3:1")

print("")
print("")
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
