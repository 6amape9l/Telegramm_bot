some_list = [7, 14, 28, 32, 32, 56]


def custom_filter(some_list: list) -> bool:
    summ = 0
    for el in some_list:
        if type(el) == int:
            if el % 7 == 0:
                summ = summ + el
    if summ > 83:
        return False
    return True


anonim = lambda s: (s.count('яЯ') + s.count('Я')) >= 23


print(anonim('яяя'))