def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt','r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print("Успешно!")


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data=input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book=f.read()
    print('Результаты поиска: ')
    print(search(tel_book,data))

def search(book: str, info: str)-> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def edit_data()-> None:
    tel_book=[show_data()]
    change_fio = input('Введите фамилию, которую хотите заменить: ')
    with open('book.txt','r', encoding='utf-8') as f:
        tel_book=f.read()
    result = search(tel_book,change_fio)
    a=len(result)
    new_tel_book = tel_book[:tel_book.index(result)] + change(result) + tel_book[tel_book.index(result)+a:]
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(f'\n{new_tel_book}')
    print(new_tel_book)

def change(text: str)-> str:
    fio = input('Введите новую фамилию: ')
    num = input('Введите новый номер телефона: ')
    if len(fio)==0:
       fio = text.split(' | ')[0]
    if len(num)==0:
       num=text.split(' | ')[1]
    return f'{fio} | {num}'

def delete_data():
    delete_fio=input("Введите фамилию, которую хотите удалить: ")
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book=f.read()
    result = search(tel_book,delete_fio)
    a=len(result)
    new_tel_book = tel_book[:tel_book.index(result)] + tel_book[tel_book.index(result)+a+1:]
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(f'{new_tel_book}')
    print(new_tel_book)
    