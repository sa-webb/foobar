# Keep track of birthdays using a dictionary.

from functools import partial


def add_birthday(b_dict):
    k = input("Enter new name ")
    v = input("Enter their bday ")
    b_dict.update({k: v})
    return b_dict


def find_birthday(b_dict):
    k = input("Enter name")
    return b_dict.get(k)

def list_birthdays(b_dict):
    return b_dict.values()


def indirect(i):
    birthdays_dictionary = {
        "Austin": "11/17/1994",
        "John": "01/17/1993",
        "Jane": "12/17/1990",
    }

    switcher = {
        0: partial(add_birthday, birthdays_dictionary),
        1: partial(find_birthday, birthdays_dictionary),
        2: partial(list_birthdays, birthdays_dictionary),
        3: lambda: '=)'
    }
    func = switcher.get(i, lambda: 'Invalid')
    return func()


while True:
    try:
        option = input('Enter option ')
        print(indirect(int(option)))
    except Exception as e:
        print(e)


# print(birthdays_dictionary.get("Austin"))
