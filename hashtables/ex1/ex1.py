#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
     # loop over the weights array
    for index in range(len(weights)):
        # get the difference between the item at the current index of the weights array and the limit passed in 
        difference = limit - weights[index]
        # check the hash table to see if the value of difference already exists as a key 
        exists_in_ht = hash_table_retrieve(ht, difference)
        # if it exists and is less than the value of the current index in the weights array
        if exists_in_ht is not None and exists_in_ht < index:
            # return tuple with value of current index and the value of exists_in_ht
            return (index, exists_in_ht)
        # else if it exists and is more than or equal the value of the current index in the weights array
        elif exists_in_ht is not None and exists_in_ht >= index:
            # return tuple with the value of exists_in_ht and value of current index 
            return (exists_in_ht, index)
        # if it does not exist yet in hash table insert it, passing the value of the weights array at the current index as the key 
        # and the value of the index as the value
        else:
            hash_table_insert(ht, weights[index], index)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))