from aiogram.types import CallbackQuery
from app.components.working_db import QuizeDatabase

db = QuizeDatabase()

async def result_quiz(callback: CallbackQuery, correct_answers: list[int]):
    # Подсчитываем количество правильных и неправильных ответов
    answer_true = correct_answers.count(1)
    answer_false = correct_answers.count(0)

    await callback.message.answer("Это был последний вопрос. Квиз завершен!")
    # await callback.message.answer(f"{grade}")
    # делю оценку на 2 так как использую 5 бальную систему 
    new_grade =  answer_true // 2
    
    grade = await db.read_database(callback.from_user.id, 'grade')
    # проверяю на больше ли текущия оценка прошлой
    final_grade = new_grade if new_grade > grade else grade
    #  записывааю результат 
    await db.write_database(callback.from_user.id, final_grade, 'grade')
    await callback.message.answer(f"Ваша оценка {new_grade} ваша прошлая оценка {grade}: правильных ответов {answer_true}, неправильных ответов {answer_false}")
