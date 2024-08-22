# create keyboard
from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

        # Создаем сборщика клавиатур типа Reply
start_keyboard= ReplyKeyboardMarkup(keyboard=[
    # Добавляем в сборщик одну кнопку
    [KeyboardButton(text="Начать игру")]
],
                          resize_keyboard=True, # min size 
                          input_field_placeholder='choice item menu') 

# V 1
# def generate_options_keyboard(answer_options, right_answer):
#   # Создаем сборщика клавиатур типа Inline
#     builder = InlineKeyboardBuilder()

#     # В цикле создаем 4 Inline кнопки, а точнее Callback-кнопки
#     for option in answer_options:
#         builder.add(InlineKeyboardButton(
#             # Текст на кнопках соответствует вариантам ответов
#             text=option,
#             # Присваиваем данные для колбэк запроса.
#             # Если ответ верный сформируется колбэк-запрос с данными 'right_answer'
#             # Если ответ неверный сформируется колбэк-запрос с данными 'wrong_answer'
#             callback_data="right_answer" if option == right_answer else "wrong_answer")
#         )
        
#     # Выводим по одной кнопке в столбик
#     builder.adjust(1)
#     return builder.as_markup()

# V 2
def generate_options_keyboard(answer_options):
    builder = InlineKeyboardBuilder()

    for index, option in enumerate(answer_options):
        # Формируем данные для callback, включая индекс ответа
        callback_data = f"confirm_answer_{index}_{option}"
        
        # Добавляем кнопку с текстом и callback_data
        builder.add(InlineKeyboardButton(
            text=f"{option}",
            callback_data=callback_data
        ))

    # Выводим по одной кнопке в столбик
    builder.adjust(1)
    return builder.as_markup()


def create_confirmation_keyboard():
    keyboard = InlineKeyboardMarkup()  # Создаем клавиатуру без параметра row_width
    confirm_button = InlineKeyboardButton("Да", callback_data="confirm_yes")
    cancel_button = InlineKeyboardButton("Нет", callback_data="confirm_no")
    keyboard.add(confirm_button, cancel_button)  # Добавляем кнопки
    return keyboard

confirmation_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data="confirm_yes")],
    [InlineKeyboardButton(text="Нет", callback_data="confirm_no")]
])


