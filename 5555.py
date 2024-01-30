import csv


def generate_hash(s):
    """
    Генерирует хэш-значение для строки s.
    :param s: Строка для генерации хэша (str)
    :return: Хэш-значение (int)
    """
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alphabet, 1)}
    p = 67
    m = int(1e9 + 9)
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value


students_with_hash = []

with open('students.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        students_with_hash.append(row)

with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['id', 'Name', 'titleProject_id', 'class', 'score']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_with_hash)