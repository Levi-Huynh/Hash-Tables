# '''
# Linked List hash table key/value pair
# '''
import time
import random
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')

"""
def djb2(key):
    # prime number
    salt = 5381
    for char in key:
        hashed = (our salt << 5) + our_salt +char
    returh hashed
"""


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key) + str(self.value)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        # self.storageDLL = DoublyLinkedList()

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.


        '''

        output = len(key) + time.time()
        return output
        # return __hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        salt = 5381
        for char in key:
            hashed = (salt << 5) + salt + char
        return hashed

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        salt = 5381
        # for char in key:
        hashed = (salt * salt) + ord(key[-1]) + len(key)
        # scrambles errything up
        hashed1 = int(hashed % self.capacity)
        print("hashed1", hashed1)
        return hashed1

       # return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        1) Hash the key ==> index
        2) If no linked list at that hash/index
        3)  make one and put it there 
        4) Else add our original key/value pair to the linked list 
        '''
        print("newkey", key)
        my_index = self._hash_mod(key)
        print("my_index", my_index)
        myDLL = DoublyLinkedList()
        if self.storage[my_index] is None:
            myDLL.add_to_head(key, value)
            self.storage[my_index] = myDLL
        elif self.storage[my_index] is not None:
            myDLL.add_to_head(key, value)
            self.storage[my_index] = myDLL
            print("test", self.storage[my_index])

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        1) Hash the key to find index
        2) go to index (the LL holding the node w/ this k/v pair lives at that index)
        3) Look at linked list, use the original key not the hash
        4) To find the right node, 
        5) use remove method 
        '''
        pass

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        my_index = self._hash_mod(key)
        if self.storage[my_index] is None:
            return None
        else:
            return self.storage[my_index].contains(key)

            # return self.storage[my_index].value  # must search thru DLL

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-1", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")

    print("")

    # Test storing beyond capacity
    print("retrieve key 1", ht.retrieve("key-0"))
    print("retrieve key 2", ht.retrieve("key-1"))
    print("retrieve key 3", ht.retrieve("key-2"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
   # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
