from app.components.questions import quiz_data
from app.components.working_db import QuizeDatabase
from app.components.keyboards import  generate_options_keyboard

db = QuizeDatabase()

async def get_question(message, user_id):

    # Запрашиваем из базы текущий индекс для вопроса
    question_index, correct_answers = await db.get_quiz_data_user(user_id)  
    # Получаем список вариантов ответа для текущего вопроса
    opts = quiz_data[question_index]['options']

    # Функция генерации кнопок для текущего вопроса квиза
    kb = generate_options_keyboard(opts)
    # Отправляем в чат сообщение с вопросом, прикрепляем сгенерированные кнопки
    await message.answer(f"{quiz_data[question_index]['question']}", reply_markup=kb)  

async def new_quiz(message):
    user_id = message.from_user.id # достали id user
    current_question_index = 0 # сбрасываем значение в 0 
    answers = [0,0,0,0,0,0,0,0,0,0]# сбрасываем значение в 0 
    await db.update_quiz_index(user_id, current_question_index, answers)
    # запрашиваем новый вопрос для квиза
    await get_question(message, user_id)
    

