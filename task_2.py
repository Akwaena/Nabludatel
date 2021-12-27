def function(n):
    d = 2
    returned = []
    while n > 0:
        c = 0
        if n > d:
            while n % d == 0:
                c += 1
                n //= d
            if c != 0:
                returned.append((d, c))
            if len(returned) > 3:
                return (), (), ()
        else:
            return (), (), ()
        d += 1
    return returned

def checker(lst):
    if lst[0] == (3, 3) and lst[1] == (5, 2) and lst[2] == (11, 3):
        return True
    return False

n = 898425
while not checker(function(n)):
    n += 1
    print(f'Итерация {n}')
print(f'Ответ: {n}')
