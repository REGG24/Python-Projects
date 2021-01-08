def count_caracters(palabra, caracteres):
    diccionario = {}
    for caracter in caracteres:
        count = 0
        for c in palabra:
            if caracter == c:
                count += 1
        diccionario[caracter] = count

    return diccionario


def count_caracters2(palabra, caracteres):
    diccionario = {}
    for caracter in caracteres:
        if caracter in diccionario:
            # if diccionario.get(caracter):
            diccionario[caracter] += 1
        else:
            if caracter in palabra:
                diccionario[caracter] = 1
            else:
                diccionario[caracter] = 0

    return diccionario


print(count_caracters2('apple', ['a', 'p', 'c']))
