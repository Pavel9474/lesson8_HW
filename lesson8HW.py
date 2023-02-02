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
task1()
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
task2()
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
task3()
# Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». 
# Вопрос и правильный ответ сохраните в файл. Реализуйте алгоритм шифрования правильного ответа.

q_a_list = [
  ['Так в старину называли сторожа городских ворот', 'ЕУГХГУЯ'],
  ['С японского это слово переводится как «Божественный ветер»', 'НГПЛНГЖКЗ'],
  ['Анисовая настойка или ликер', 'ГДФЗРХ'],
  ['Название этого растения произошло от греческого «порождающий чистоту»', 'ДГНОГЙГР'],
  ['Что изготавливал в старину скудельник?', 'НЦЕЫЛР'],
  ['Противовес «естественного отбора», созданный человеком', 'ФЗОЗНЩЛВ'],
  ['Что считается самой распространенной в мире незаразной болезнью', 'НГУЛЗФ'],
]
def cesar(word):
    alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    a = 3
    b = word.upper()
    res = ''
    for i in b:
        res += alpha[(alpha.index(i) - a) % len(alpha)]
    return res

def show_answer():
    global answer
    print(' | '.join(answer).upper())

q_a = random.choice(q_a_list)
question = q_a[0]
correct_answer = cesar(q_a[1])
answer = ['*'] * len(correct_answer)
print('Вопрос:')
print(question)

win = False
while not win:
  show_answer()
  print('\nНазовите букву или слово')
  letter = input()
  if len(letter) > 1:
    if letter.upper() == correct_answer.upper():
      win = True
      print('Вы победили')
    else:
      print('Оказия!! Переход хода')
  else:
    if not letter.upper() in correct_answer.upper():
      print('Нет такой буквы\nПереход хода')
    else:
      print('Есть такая буква!')
      print(f'Откройте нам букву {letter.upper()}')
      for i in range(len(correct_answer)):
        if letter.upper() == correct_answer[i].upper():
          answer[i] = letter.upper()         
