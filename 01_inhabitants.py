# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код


import room_1, room_2

print('В комнате', room_1.__name__, 'живут:', ','.join(room_1.folks))

print('В комнате', room_2.__name__, 'живут:', ','.join(room_2.folks))
