#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)                   


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # firstly, insert all tickets in the tickets list into the hashtable using insert method 
    # passing in the ticket source as the key and the ticket destination as the value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # we know that the very first ticket is going to have to have a source on "NONE"
    # declare variable 'source' and initialize it to "NONE"
    source = "NONE"
    # now loop over the route array 
    for i in range(len(route)):
        # at every index, set the value equal to what is returned from retrieving from the hash table, passing the current value of source as the key to look for
        curr_ticket = hash_table_retrieve(hashtable, source)
        # set the value of source to the value of curr_ticket, will be used as the key to retrieve the next ticket from hashtable
        source = curr_ticket
        # set the value in the route array at the current index equal to the curr_ticket
        route[i] = curr_ticket
   
    # return the route 
    return route