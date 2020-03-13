#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for zeroth in range(0, length):
        first = hash_table_retrieve(ht, (limit-weights[zeroth]))
        print('hello this is first', first)
        if first != None:
            answer = (zeroth, first)
            print('zeroth and first', zeroth,first)
            print('answer', answer)
            return answer 
        else:
            hash_table_insert(ht, weights[zeroth], zeroth)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
