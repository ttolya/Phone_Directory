import json

SPRAVOCHNIK_FILE = "spravochnik.json"

def load_spravochnik():
    try:
        with open(SPRAVOCHNIK_FILE, "r") as file:
            spravochnik = json.load(file)
    except FileNotFoundError:
        spravochnik = []
    return spravochnik

def save_spravochnik(spravochnik):
    with open(SPRAVOCHNIK_FILE, "w") as file:
        json.dump(spravochnik, file)

def show_record(record):
    print("Фамилия:", record.get("фамилия"))
    print("Имя:", record.get("имя"))
    print("Отчество:", record.get("отчество"))
    print("Название организации:", record.get("организация"))
    print("Рабочий телефон:", record.get("телефон_рабочий"))
    print("Личный телефон:", record.get("телефон_личный"))
    print("-" * 20)

def show_records(records, page_num, per_page):
    start_index = (page_num - 1) * per_page
    end_index = min(start_index + per_page, len(records))
    for i in range(start_index, end_index):
        show_record(records[i])

def add_record(spravochnik):
    record = {}
    record["фамилия"] = input("Введите фамилию: ")
    record["имя"] = input("Введите имя: ")
    record["отчество"] = input("Введите отчество: ")
    record["организация"] = input("Введите название организации: ")
    record["телефон_рабочий"] = input("Введите рабочий телефон: ")
    record["телефон_личный"] = input("Введите личный телефон: ")
    spravochnik.append(record)
    save_spravochnik(spravochnik)
    print("Запись успешно добавлена.")

def edit_record(spravochnik):
    search_term = input("Введите фамилию или организацию для поиска записи: ").lower()
    found_records = []
    for record in spravochnik:
        if search_term in record["фамилия"].lower() or search_term in record["организация"].lower():
            found_records.append(record)
    if not found_records:
        print("Запись не найдена.")
        return
    for i, record in enumerate(found_records):
        print(i+1, end=". ")
        show_record(record)
    choice = int(input("Выберите номер записи для редактирования: ")) - 1
    if 0 <= choice < len(found_records):
        field = input("Введите название поля для редактирования: ").lower()
        if field in found_records[choice]:
            new_value = input(f"Введите новое значение для поля '{field}': ")
            found_records[choice][field] = new_value
            save_spravochnik(spravochnik)
            print("Запись успешно отредактирована.")
        else:
            print("Указанное поле не существует.")
    else:
        print("Некорректный выбор.")

def search_records(spravochnik):
    search_term = input("Введите фамилию или организацию для поиска записи: ").lower()
    found_records = []
    for record in spravochnik:
        if search_term in record["фамилия"].lower() or search_term in record["организация"].lower():
            found_records.append(record)
    if not found_records:
        print("Запись не найдена.")
    else:
        for record in found_records:
            show_record(record)

def main():
    spravochnik = load_spravochnik()
    while True:
        print("\nМеню:")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записи")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            page_num = int(input("Введите номер страницы: "))
            per_page = int(input("Введите количество записей на странице: "))
            show_records(spravochnik, page_num, per_page)
        elif choice == "2":
            add_record(spravochnik)
        elif choice == "3":
            edit_record(spravochnik)
        elif choice == "4":
            search_records(spravochnik)
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод.")

if __name__ == "__main__":
    main()