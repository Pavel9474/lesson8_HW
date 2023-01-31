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

def show_display_word():
  global display_word
  print(' | '.join(display_word).upper())

q_a = random.choice(db)
question = q_a[0]
correct_answer = q_a[1]
display_word = ['*'] * len(correct_answer)
print('Вопрос:')
print(question)


win = False
while not win:
  show_display_word()
  print('\nНазовите букву или слово')
  a = input()
  if len(a) > 1:
    #  Сценарий, если ввели слово
    if a.upper() == correct_answer.upper():
      #  Если слово совпадает с правильным
      win = True
      print('Вы победили')
    else:
      #  Если слово не совпадает с правильным
      print('Вы ошиблись, переход хода')
  else:
    #  Сценарий, если ввели букву
    if not a.upper() in correct_answer.upper():
      #  Если такой буквы нет в слове
      print('Такой буквы нет\nПереход хода')
    else:
      #  Если буква есть
      print('Есть такая буква!')
      print(f'Откройте нам букву {a.upper()}')
      for i in range(len(correct_answer)):
        if a.upper() == correct_answer[i].upper():
          display_word[i] = a.upper()
show_display_word()