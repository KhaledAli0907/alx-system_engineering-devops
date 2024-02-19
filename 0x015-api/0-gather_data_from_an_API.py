#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from sys import argv
from requests import get


def main():
    res = get("https://jsonplaceholder.typicode.com/todos/")
    res2 = get("https://jsonplaceholder.typicode.com/users")
    todos = res.json()
    users = res2.json()
    completed = 0
    total = 0
    tasks = []

    for user in users:
        if user.get("id") == int(argv[1]):
            employee = user.get("name")

    for todo in todos:
        if todo.get("userId") == int(argv[1]):
            total += 1

        if todo.get("completed") == True:
            completed += 1
            tasks.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed, total))

    for task in tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    main()
