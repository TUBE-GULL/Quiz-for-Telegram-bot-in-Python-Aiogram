# Структура квиза
#1.  question - вопрос
#2.  options - варианты ответов
#3.  correct_option - индекс правильного ответа

quiz_data = [
    {# question 1
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {# question 2
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {# question 3
        'question': "В каком типе данных хранится 'ключ' и 'значения'?",
        'options': ['list', 'dict', 'set', 'tuple'],
        'correct_option': 1
    },
    {# question 4
        'question': 'В каком типе данных не бывает одинаковых значений?',
        'options': ['list', 'dict', 'set', 'tuple'],
        'correct_option': 2
    },
    {# question 5
        'question': 'Как получить значение из словаря, если ключ может отсутствовать, без возникновения ошибки?',
        'options': ['update', 'pop', 'get', 'len'],
        'correct_option': 2
    },
    {# question 6
        'question': 'Как правильно сделать копию объекта, если у него есть не один уровень вложенных структур?',
        'options': ['object2 = object1', 'deepcopy', 'len', 'copy'],
        'correct_option': 1
    },
    {# question 7
        'question': 'Кто из представленных вариантов не является логическим оператором?',
        'options': ['or', 'is', 'and', 'not'],
        'correct_option': 1
    },
    {# question 8
        'question': 'Как правильно строятся условные инструкции?',
        'options': ['if, elif, else', 'if, elif, elif', 'if, if, else', 'elif, elif, else'],
        'correct_option': 0
    },
    {# question 9
        'question': 'Сколько видов циклов в Python?',
        'options': ['1: for in', '4: array, for in, if else, def', '3: for in, def, while', '2: for in, while'],
        'correct_option': 3
    },
    {# question 10
        'question': 'Как создать анонимную функцию в Python?',
        'options': ['lambda', 'def', 'anonymous', 'func'],
        'correct_option': 0
    }
]
