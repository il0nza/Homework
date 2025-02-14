from plan_text import *
import math as m


# добавить задание
def start_add_task(week: dict) -> None:
    choice_day = input(CHOICE_DAY_TO_ADD_TASK)
    if choice_day in week:
        task = input(INPUT_TASK_TEXT)
        week[choice_day].append(task)
        print(CORRECT)
    else:
        print(NO_SEARCH_DAY)


# вывести задания на день или на неделю
def start_output_task(week: dict) -> None:
    day_or_week = input(DAY_OR_WEEK)
    if day_or_week == '1':
        choice_day = input(CHOICE_DAY_TO_ADD_TASK)
        if choice_day in week:
            print_day(week, choice_day)
        else:
            print(NO_SEARCH_DAY)
    elif day_or_week == '2':
        print_week(week)
    else:
        print(NO_SEARCH_COMMAND)


# находим самое длинное задание
def get_max_len(tasks: list) -> int:
    if len(tasks) != 0:
        max_len = len(tasks[0])
        for task in tasks:
            if len(task) > max_len:
                max_len = len(task)
        return max_len
    else:
        return 0


# вывод заданий на день
def print_day(week: dict, day: str) -> None:
    if get_max_len(week[day]) == 0:
        print(NOTHING)
    else:
        max_len = get_max_len(week[day]) + 2
        print('+', '-' * max_len, '+')
        print('|', ' ' * (max_len // 2 - 2 if max_len % 2 == 0 else max_len // 2 - 1), day,
              ' ' * (max_len // 2 - 2 if max_len % 2 == 0 else max_len // 2 - 2), '|')
        print('|', ' ' * max_len, '|')
        for i in range(len(week[day])):
            x = max_len - len(week[day][i])
            if x != 2:
                print('|', '*', week[day][i], ' ' * (x - 3), '|')
            else:
                print('|', '*', week[day][i], '|')
        print('|', ' ' * max_len, '|')
        print('+', '-' * max_len, '+')


# вывод заданий на неделю
def print_week(week: dict) -> None:
    print('Планы на неделю')
    for j in week:
        if len(week[j]) != 0:
            print_day(week, j)
        else:
            print()
            print(j, ' -- ', 'планов нет')
            print()


# удаление задач
def start_remove_task(week: dict) -> None:
    print()
    day_del = input(DEL_DAY)
    if day_del in week:
        if len(week[day_del]) != 0:
            print(TASK)
            print_day(week, day_del)
            del_task = input(DEL_TASK)
            try:
                if len(week[day_del]) >= int(del_task):
                    week[day_del].pop(int(del_task) - 1)
                    print(CORRECT_DEL)
                else:
                    print(ERROR_NUM)
            except ValueError:
                print(ERROR)
        else:
            print(NOTHING)
    else:
        print(NO_SEARCH_DAY)


def main():
    week = {
        'пн': [],
        'вт': [],
        'ср': [],
        'чт': [],
        'пт': [],
        'сб': [],
        'вс': []
    }

    print(HELLO_PLAN_TEXT)
    print(FUNCTIONS_PRINT)
    choice = input(CHOICE_PRINT)
    while choice != '4':
        if choice == '1':
            start_add_task(week)
        elif choice == '2':
            start_output_task(week)
        elif choice == '3':
            start_remove_task(week)
        else:
            print(NO_SEARCH_COMMAND)

        print(FUNCTIONS_PRINT)
        choice = input(CHOICE_PRINT)


main()
