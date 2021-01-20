"""
def find_unique_numbers(numbers):
    recorridos = set()
    unique = set()
    for number in numbers:
        if number not in recorridos:
            recorridos.add(number)
            unique.add(number)
        else:
            if number in unique:
                unique.remove(number)
    return list(unique)


print(find_unique_numbers([1, 2, 1, 3]))
"""

"""
def find_all_hobbyists(hobby, hobbies):
    names = []
    for key in hobbies:
        print(key)
        print(hobbies[key])
        for hobby_item in hobbies[key]:
            print(hobby_item)
            if hobby_item == hobby:
                names.append(key)
    return names


hobbies = {
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

print(find_all_hobbyists('Yoga', hobbies))
"""


"""
import json
def sort_by_price_ascending(json_string):
    lista_dict = json.loads(json_string)
    lista = []
    for key in lista_dict:
        name = ""
        price = 0
        count = 1
        for key2 in key:
            if count == 1:
                name = key[key2]
            else:
                price = key[key2]
            count += 1

        lista.append((name, price))

    sorted_list = sorted(lista, key=lambda x: x[1])
    final_string = "["
    for i in range(len(sorted_list)):
        answer = {}
        answer['name'] = sorted_list[i][0]
        answer['price'] = sorted_list[i][1]
        print(json.dumps(answer))
        if i < len(sorted_list) - 1:
            final_string += json.dumps(answer) + ","
        else:
            final_string += json.dumps(answer)

    final_string += "]"

    return final_string


print(sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
"""
"""
def PhoneNumber(N):

    # this is default OUTPUT. You can change it.
    result = ""
    chars = []
    # write your Logic here:
    positions = []

    for i in range(len(N)):
        print(N[i])
        if N[i] == '?':
            positions.append(i)
            chars.append('0')
        else:
            chars.append(N[i])

    number = int(''.join(chars))
    min = 9999999999

    if number % 3 == 0:
        return str(number)

    for pos in reversed(positions):
        for i in range(0, 10):
            chars[pos] = str(i)
            print(chars)
            numberAUX = int(''.join(chars))
            if numberAUX % 3 == 0:
                if numberAUX < min:
                    min = numberAUX

    return str(min)


# INPUT [uncomment & modify if required]
N = "5?9?3?????"

# OUTPUT [uncomment & modify if required]
PhoneNumber(N)
"""
