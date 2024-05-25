import requests
import sqlite3

connection = sqlite3.connect('Links.db', 5)
cursor = connection.cursor()

func = ['1. Make new link', '2. Print what i found', '3. delete link']

# cursor.execute(
#     'create table Table_links (Links TEXT), (Word TEXT), (Count TEXT);'
# )

def adder():
    enter = input('Enter your link -- ')
    text_to_search = input('Enter your word to search -- ')
    response = requests.get(enter)
    text = response.text
    count = text.count(text_to_search)

    cursor.execute(
        f'insert into Table_links (Links, Word, Count) values (?,?,?);', (enter, text_to_search, count)
    )
    print(f'{enter}, {text_to_search}, {count}')

def printer():
    cursor.execute("SELECT * FROM Table_links;")
    connection.commit()
    res = cursor.fetchall()
    print(res)

def delete_link():
    which_is = int(input('Which is --'))
    cursor.execute(f"DELETE FROM Table_links WHERE rowid={which_is};")

while True:
    print(func)
    do_func = int(input('-- '))

    if do_func == 1:
        adder()
    elif do_func == 2:
        printer()
    elif do_func == 3:
        delete_link()