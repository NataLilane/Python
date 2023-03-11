

# Phone_book

print(' 1. Открыть файл\n 2. Сохранить файл\n 3. Показать все контакты\n 4. Создать контакт\n 5. Изменить контакт\n 6. Найти контакт\n 7. Удалить контакт\n 8. Выход')
path = 'Семинары\Seminar8\справочник.txt'
phone_book = []
new_file = []

def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')


def search_contact(phone_book):
    search = input('Введите ключевой элемент: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)


def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))

def edit_contact():
    show_contacts(phone_book)
    num_con = int(input('Введите номер контакта, который необходимо изменить: '))
    old_con = phone_book[num_con - 1]
    print('; '.join(str(i) for i in old_con))
    
    phone_book.pop(num_con - 1)
    name = input('Введите новое имя: ')
    phone = input('Введите новый телефон: ')
    comment = input('Введите новый комементарий: ')
    phone_book.insert((num_con - 1), (list([name, phone, comment])))
    show_contacts(phone_book)


# def save_file(path, data):
#         file = open(path, 'w', encoding='UTF-8')
#         file.write(data)
#         file.close()




def delete_contact():
    num_con = int(input('Введите номер контакта, который необходимо удалить: '))
    old_con = phone_book[num_con - 1]
    string = old_con
    print('; ' .join(str(i) for i in old_con))
    a = input('Удалить?   ')
    if a == 'да':
        phone_book.pop(num_con - 1)
        new_file.append(show_contacts(phone_book))
        print(new_file)
    #print(' '.join(new_file))  
    #save_file(path, ' '.join(new_file))



while True:
    number = int(input('Введите пункт меню: '))

    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        # case 2:
        #     save_file(path, data)
        #    print('Изменения сохранены')
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            edit_contact()
        case 6:
            search_contact(phone_book)
        case 7:
            delete_contact()
        case 8:
            break
print('До встречи!')



