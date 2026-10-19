from csv import reader
import os
from unittest import case

def open_table():
    try:
        with open('books.csv', 'r', encoding='cp1251') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            return table
    except FileNotFoundError:
        print('Файл не найден!')
        return 0

table=open_table()[1:]

def notes():
    c=0
    l=int(input())
    for row in table:
            if len(row[1]) > l:
                c += 1
    print(f'Количество записей с названием длиннее {l} символов: {c}')



def search_author(table):
    Aut=input('Ведите автора книги от 2018 года: ').strip().lower()
    Aut=Aut.replace('.',' ')
    Proverka=Aut.replace(' ','')
    if Aut=='':
        return 'Ошибка'
    if Proverka.isalpha()==False:
        return 'Ошибка'
    flag=0
    for row in table:
        date = row[6].split(' ')[0]
        try:
            year=int(date[-4:])
        except ValueError:
            continue
        Prow=row[3].replace(' ','').strip().lower()
        if Aut==Prow and year>=2018:
            print(f'{row[3]} -- {row[1][1:]}')
            flag+=1
    if flag==0:
        print("Ничего не найдено или книга выпущена раньше 2018г.")


def list(table):
    output=open('../book_list.txt', 'w')
    n=1
    for row in table:
        if n>20:
            break
        date = row[6].split(' ')[0]
        year = int(date[-4:])
        output.write(f' {n}. {row[3]}. {row[1][1:]} - {year} \n')
        n+=1
    output.close()

# notes()
# search_author(table)
# list(table)