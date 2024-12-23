from itertools import *

answer = 0

for i in product("ПРИВЕТ", repeat=5): #Перебираем все 5-буквенные слова состоящие из букв ПРИВЕТ,
    a = "".join(i) #Переводим в строку
    a_reverse = a[::-1] # Получаем слово задом наперед
    if a == a_reverse:
        answer += 1 # Если слово палиндром, то записываем +1 к ответу
print(answer) # Выводим ответ