# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. 
# Определите группу с наилучшим средним баллом.
import random
import statistics
def task1():
    n, m = 5, 25
    matrix = [[random.randint(1, 5) for j in range(m)] for i in range(n)]
    aver=[]
    for i in matrix:
        aver.append(statistics.mean(i))
        print(i)
    print(f'Наибольший средний балл у группы: {aver.index(max(aver))} и равен {max(aver)}')
# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной 
# диагонали матрицы.
def task2():
    sum_main=0
    n, m = 5, 5
    matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
    for i in matrix:
        print(i)
    for i in range(n):
        sum_main+=matrix[i][i]
    for i in matrix:
     if sum(i)>=sum_main:
        print(f'Сумма элементов строки {matrix.index(i)} равна {sum(i)} и превышает сумму элементов главной диагонали {sum_main}')     

# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
#  Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. 
# Выведите их даты.
def task3():
    m=31
    temperatures=[[random.randint(8, 20) for j in range(31)], [random.randint(17, 28) for j in range(30)], [random.randint(20, 29) for j in range(31)], [random.randint(19, 26) for j in range(30)], [random.randint(13, 23) for j in range(30)]]
    mounth_name=['Мая', 'Июня', 'Июля', 'Августа', 'Сентября']
    for i in temperatures:
        print(i)
    for i in temperatures:
        start_index=0
        end_index=6
        period_values=[]
        while end_index!=len(i):
            t=sum(i[start_index:end_index])/7
            period_values.append(round(t,1))
            start_index+=1
            end_index+=1
        max_value=max(period_values)
        min_value=min(period_values)
        print(f'Самый жаркий 7 дневный период {mounth_name[temperatures.index(i)]}: {period_values.index(max_value)}-{period_values.index(max_value)+7}, Самый холодный 7 дневный период {mounth_name[temperatures.index(i)]}:{period_values.index(min_value)}-{period_values.index(min_value)+7}')
# Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». 
# Вопрос и правильный ответ сохраните в файл. Реализуйте алгоритм шифрования правильного ответа.
def task4():
    def get_question():
        with open('questions.txt', 'r', encoding='utf-8') as f:
            question_list=f.read().splitlines()
        number_question=random.randrange(0,len(question_list))
        question_answer=str(question_list[number_question])
        for i in range(0,len(question_answer)):
            if question_answer[i]==':':
                question=question_answer[0:i]
                answer=question_answer[i+1:len(question_answer)]
        return answer, question
    answer, question=get_question()
    print(question)
    print(answer)
    current_view=[]
    for i in range(0, len(answer)):
        current_view.append('*')
        print(''.join(current_view))
    while True:
        user=input('Угадайте букву или назовите слово')
        if user==answer:
            print('Вы правильно угадали слово!'); break
        if (user in answer):
            print('Есть такая буква!')
            for i in range(0, len(answer)):
                if answer[i]==user:
                    current_view[i]=user
                    current_view[i]==''.join(current_view)
        else:
            print('Вы не угадали')
        if current_view == answer: 
            print('Вы правильно угадали все буквы'); break
        print(answer)
task4()
import random
db = [
  ['Живопись по сырой штукатурке водяными красками', 'фреска'],
  ['С японского это слово переводится как «Божественный ветер»', 'Камикадзе'],
  ['Как называлась раньше карточная масть пики', 'Лопата'],
  ['Эта сказочная героиня была описана в греческой истории под именем Родопис', 'Золушка'],
  ['Какой музыкальный инструмент имеет голову, гребень, натянутый обруч и подлокотник', 'Банджо'],
  ['Геометрический термин, широко используемый в характеристике современной техники', 'Диагональ'],
  ['Детеныши этого животного приобретают пол в зависимости от температуры окружающей среды', 'Крокодил'],
]

# def show_display_word():
#   global display_word
#   print(' | '.join(display_word).upper())

# q_a = random.choice(db)
# question = q_a[0]
# correct_answer = q_a[1]
# display_word = ['*'] * len(correct_answer)
# print('Вопрос:')
# print(question)


# win = False
# while not win:
#   show_display_word()
#   print('\nНазовите букву или слово')
#   a = input()
#   if len(a) > 1:
#     #  Сценарий, если ввели слово
#     if a.upper() == correct_answer.upper():
#       #  Если слово совпадает с правильным
#       win = True
#       print('Вы победили')
#     else:
#       #  Если слово не совпадает с правильным
#       print('Вы ошиблись, переход хода')
#   else:
#     #  Сценарий, если ввели букву
#     if not a.upper() in correct_answer.upper():
#       #  Если такой буквы нет в слове
#       print('Такой буквы нет\nПереход хода')
#     else:
#       #  Если буква есть
#       print('Есть такая буква!')
#       print(f'Откройте нам букву {a.upper()}')
#       for i in range(len(correct_answer)):
#         if a.upper() == correct_answer[i].upper():
#           display_word[i] = a.upper()
# show_display_word()
