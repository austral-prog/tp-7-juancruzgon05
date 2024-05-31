def index_of_by_index(word, list, index):
    for posicion, elemento in enumerate(list):
        if posicion >= index:
            if elemento == word:
                return posicion
    else:
        return -1

def index_of_empty(list):
    for posicion,elemento in enumerate(list):
        if elemento == "":
            return posicion
    return -1

def index_of(word, list):
    for indice, elemento in enumerate(list):
        if elemento == word:
            return indice
    else:
        return -1

def put(word, list):
    for posicion in range(0, len(list)):
        if list[posicion] == "":
            list[posicion] = word
            return posicion
    return -1

def remove(word, list):
    var = 0
    for posicion,elemento in enumerate(list):
        if elemento == word:
            list[posicion] = ""
            var = var + 1
    return var
