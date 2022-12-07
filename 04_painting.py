# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

import simple_draw as sd
sd.resolution=(1300,700)
from draw_elements.tree import draw_branches_v2
from draw_elements.rainbow import rainbow
from draw_elements.sun import sun
from draw_elements.house import house
import draw_elements.man


rainbow()

root_point_1 = sd.get_point(1000, 30)
draw_branches_v2(start_point=root_point_1,angle=90,branch_length=100)

root_point_1 = sd.get_point(800, 450)
draw_branches_v2(start_point=root_point_1,angle=90,branch_length=50)

point_1 = sd.get_point(0, 0)
point_2 = sd.get_point(1300, 30)
sd.rectangle(point_1,point_2,[140,70,20])

point_sun = sd.get_point(100,620)
sun(point_sun)
house(50,30,550,430)

draw_elements.man.man(600,100,70)

sd.pause()