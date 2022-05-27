#генерация
import random

def generate_array(length=100):  # генерируем случайный массив
    array = []
    while len(array) < length:
        array.append(random.randint(0, 100))
    return array
#для хэша
class ClassForRehash:
    def __init__(self, value1):
        self.value1 = value1
        self.hash = int((((value1 % ClassForRehash.MAX_HASH_TABLE) * 331) & 127) % ClassForRehash.MAX_HASH_TABLE)

    MAX_HASH_TABLE = 8

# просто рехэширование
class SimpleRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = element
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, element.hash))
            return

        """""
        простое рехеширование
        """""
        new_hash = original_hash + 1
        while new_hash != original_hash:
            if new_hash >= len(self.table):
                new_hash = 0
                continue
            if self.table[new_hash] is None:
                element.hash = new_hash
                self.table[new_hash] = element
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                return
            new_hash += 1
        print("таблица заполнена!")
        return
#вывод
simple_re = SimpleRehashTable(ClassForRehash.MAX_HASH_TABLE)
for i in range(len(simple_re.table) + 2):
    simple_re.add_el(ClassForRehash(random.randint(0, 8)))


#случайное

class RandomRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = element
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, original_hash))
            return

        """""
        случайное рехеширование
        """""
        table_len = len(self.table)
        r = 1
        for ii in range(10):  # range(число попыток определить новый хеш)
            r *= 5
            r = r % (4 * table_len)
            new_hash = r // 4
            if self.table[new_hash] is None:
                element.hash = new_hash
                self.table[new_hash] = element
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                return
        print("Не удалось найти свободный хеш в таблице!")
        return
#вывод
random_re = RandomRehashTable(ClassForRehash.MAX_HASH_TABLE)
for i in range(len(random_re.table) + 2):
    random_re.add_el(ClassForRehash(random.randint(0, 9)))

#метод цепочек
class ChainRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        """""
        метод цепочек
        """""
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = [element]
            return
        else:
            length = len(self.table[original_hash])
            self.table[original_hash].append(element)
            return

# вывод
chain_re = ChainRehashTable(ClassForRehash.MAX_HASH_TABLE)
for i in range(len(chain_re.table) + 2):
    chain_re.add_el(ClassForRehash(random.randint(0, 9)))
hash = 0
for x in chain_re.table:  # вывод хеш таблицы для метода цепочек
    print("[hash: %i]" % hash, end=" ")
    if x is None:
        print("Пусто")
    else:
        for y in x:
            print(y.value1, end=" ")
        print("")
    hash += 1