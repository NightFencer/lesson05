# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1.room1 import folks as fcsh1r1
from district.central_street.house1.room2 import folks as fcsh1r2
from district.central_street.house2.room1 import folks as fcsh2r1
from district.central_street.house2.room2 import folks as fcsh2r2

from district.soviet_street.house1.room1 import folks as fssh1r1
from district.soviet_street.house1.room2 import folks as fssh1r2
from district.soviet_street.house2.room1 import folks as fssh2r1
from district.soviet_street.house2.room2 import folks as fssh2r2
all_sitizens= fcsh1r1+fcsh1r2+fcsh2r1+fcsh2r2+fssh1r1+fssh1r2+fssh2r1+fssh2r2
print('На районе живут:',','.join(all_sitizens*10))



