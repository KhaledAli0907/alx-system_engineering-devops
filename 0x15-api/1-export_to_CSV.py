#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

import csv
from requests import get
from sys import argv


def main():
    res = get("https://jsonplaceholder.typicode.com/todos/")
    res2 = get("https://jsonplaceholder.typicode.com/users")
    todos = res.json()
    users = res2.json()

    userid = int(argv[1])

    for user in users:
        if user['id'] == userid:
            employee = user['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)


if __name__ == '__main':
    main()
