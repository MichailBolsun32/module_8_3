"""Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:

Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
Возвращает True, если корректный, в других случаях выбрасывает исключение.
Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
Возвращает True, если корректный, в других случаях выбрасывает исключение.
Уровень доступа private.

Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
объекты которых обладают атрибутом message - сообщение,
которое будет выводиться при выбрасывании исключения.


Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin

Выбрасывает исключение IncorrectVinNumber с сообщением
'Некорректный тип vin номер', если передано не целое число.
(тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением
'Неверный диапазон для vin номера', если переданное число находится не в диапазоне
от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.

__is_valid_numbers

Выбрасывает исключение IncorrectCarNumbers с сообщением
'Некорректный тип данных для номеров', если передана не строка.
(тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.


ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
(в __init__ при объявлении атрибутов __vin и __numbers)."""

#Определяет сообщение которое будет выбрасываться при ошибки VIN
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


# Определяет сообщение которое будет выбрасываться при ошибки номера
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car(IncorrectVinNumber):
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        else:
            self.__vin = None

        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        else:
            self.__numbers = None

    def __is_valid_vin(self, vin):
        if isinstance(vin, int):
            if 1000000 <= vin <= 9999999:
                return True
            else: #создаем исключения
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:#создаем исключения
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) != 6:#создаем исключения
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return str
        else:#создаем исключения
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')