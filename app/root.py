from aiogram import F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,CallbackQuery

#import Models 
from app.components.working_db import QuizeDatabase
from app.components.fun_questions import new_quiz, get_question
from app.components.keyboards import start_keyboard,confirmation_keyboard
from app.components.questions import quiz_data
from app.components.result_quiz import result_quiz

router = Router()
db = QuizeDatabase()

@router.message(CommandStart())
async def start(message:Message):
    # Прикрепляем кнопки к сообщению
    await message.answer("Добро пожаловать в квиз", reply_markup=start_keyboard)

    
@router.message(Command('quiz'))
async def cmd_quiz(message:Message):
    await message.answer("Давайте начнем квиз Первый вопрос: ...")
    

@router.message(F.text == "Начать игру")
@router.message(Command('quiz'))
async def cmd_quiz(message: Message):
    await message.answer(f"Давайте начнем квиз")
    await new_quiz(message)


@router.callback_query(F.data.startswith("confirm_answer"))
async def confirm_answer(callback: CallbackQuery):
    _, index, answer,answer_user = callback.data.split("_")
    # Сохраняем данные о выборе пользователя
    await db.write_database(callback.from_user.id, answer, 'choice')

    # Отправляем пользователю вопрос на подтверждение
    await callback.message.answer(
        f"Вы уверены {answer_user} ?",
        reply_markup=confirmation_keyboard
    )
    

@router.callback_query(F.data == "confirm_yes")
async def wrong_answer(callback: CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )

    # Получение Данные о пользователе 
    question_index, correct_answers = await db.get_quiz_data_user(callback.from_user.id)
    choice = await db.read_database(callback.from_user.id, 'choice')
    correct_option = quiz_data[question_index]['correct_option']


    if quiz_data[question_index]['correct_option'] == choice:
        await callback.message.answer("Верно!")
        correct_answers[question_index] = 1
    else:    
        await callback.message.answer(f"Неправильно. Правильный ответ: {quiz_data[question_index]['options'][correct_option]}")
        correct_answers[question_index] = 0
    
    # Обновление номера текущего вопроса в базе данных
    question_index += 1
    await db.update_quiz_index(callback.from_user.id, question_index, correct_answers)

    # Проверяем достигнут ли конец тест на Pythonа
    if question_index < len(quiz_data): 
        # Следующий вопрос
        await get_question(callback.message, callback.from_user.id)
    else: # Уведомление об окончании квиза
        await result_quiz(callback, correct_answers)
              
       
@router.callback_query(F.data == "confirm_no")
async def change_answer(callback: CallbackQuery):
    # Повторно отправляем текущий вопрос пользователю
    await get_question(callback.message, callback.from_user.id)