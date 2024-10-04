'''
Практическое задание по работе в Pycharm - "Переменные".

Цель: научиться правильно называть переменные и взаимодействовать с ними.

Задача:

Напишите 4 переменных которые буду обозначать следующие данные:

Количество выполненных ДЗ (запишите значение 12)
Количество затраченных часов (запишите значение 1.5)
Название курса (запишите значение 'Python')
Время на одно задание (вычислить используя 1 и 2 переменные)
Выведите на экран(в консоль), используя переменные, следующую строку:

Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

Пример написанного кода:

first_name = 'Vasya'

apple_count = 10

second_name = 'Petya'

orange_count = 15

print(first_name, 'дал', second_name, apple_count, 'яблок и', orange_count, 'апельсинов')

Результат выполнения кода:

Vasya дал Petya 10 яблок и 15 апельсинов

Примечания:

Для вывода значений на экран используйте функцию print(a, b, c), где a, b, c - данные которые выводятся на экран.
Для названия переменных используйте только: латинские буквы, не начинайте запись с числа, пишите в змеином регистре(разделяя слова символом '_')
Пробелы между словами и символами ':' ',' можно ставить на своё усмотрение.
'''
quantity_hours = 12
hours_spent = 1.5
course_name = "Python"
print("Курс: ",course_name,", всего задач: ",quantity_hours,", затрачено часов: ",hours_spent,", среднее время выполнения: ",hours_spent/quantity_hours,"ч.",sep='')