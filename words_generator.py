from typing import Any


class WordsGenerator:
    @staticmethod
    def generate_words():
        words_list: list[tuple[str, str, str] | Any] = [
            ('Hello', 'Привет', 'Сущ.'),
            ('Cat', 'Кошка', 'Сущ.'),
            ('Dog', 'Собака', 'Сущ.'),
            ('House', 'Дом', 'Сущ.'),
            ('Book', 'Книга', 'Сущ.'),
            ('Run', 'Бежать', 'Гл.'),
            ('Eat', 'Есть', 'Гл.'),
            ('Happy', 'Счастливый', 'Прил.'),
            ('Big', 'Большой', 'Прил.'),
            ('Beautiful', 'Красивый', 'Прил.'),
            ('I', 'Я', 'Мест.'),
            ('You', 'Ты', 'Мест.'),
            ('He', 'Он', 'Мест.'),
            ('She', 'Она', 'Мест.'),
            ('It', 'Оно', 'Мест.')
        ]
        return words_list
