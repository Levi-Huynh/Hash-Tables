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

        These are bitwise shift operators.

        Quoting from the docs:

        x << y
        Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

            x >> y
djb2 is one of the best string hash functions i know. it has excellent distribution and speed on many different sets of keys and table sizes. you are not likely to do better
with one of the "well known" functions such as PJW, K&R[1],
        '''
        salt = 5381
        for char in key:
            # ORD RETURNS unicode point / INT
            hashed = ((salt << 5) + hashed) + ord(char)

        return hashed

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        hashed = 5381

        for char in key:
            hashed = ((hashed << 5) + hashed) + ord(char)

        return hashed % self.capacity

       # return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        1) Hash the key ==> index
        2) If no linked list at that hash/index
        3)  make one and put it there
        4) Else add our original key/value pair to the linked list

     # print("START INSERT HERE. newkey", key)
        my_index = self._hash_mod(key)
        # print("my_index", my_index)

        # create an instance of LinkedPair using k,v
        _kv = LinkedPair(key, value)

        # memorize pseduo..not just the actual code (is it best & conventional to always allocate 1 space in next LL node )??
        # create memory space for self.strorage[my_index] & store in _kv.next.
        # next default is none, setting this to temp var here which is none, creating space
        # currently self.storage[my_index] at any index equals none #allocate space to next node, giving None value
        _kv.next = self.storage[my_index]
        # print("SELF.STORAGE[my_index]:",
        # self.storage[my_index], _kv.next, "kv.next here")

        # set self.storage[my_index] to the newly created LinkedPair(k, v)
        # self.storage[my_index] becomes my storage variable here, & we give it the `value` of whatever LinkedPair tuple is
        self.storage[my_index] = _kv

        """
        index = self._hash_mod(key)
        curr = self.storage[index]
        prev = None
        # iterate through based on condition:
        # while iterating if curr.key ! = key
        while curr is not None and curr.key != key:
            prev = curr
            curr = prev.next

        if curr is not None:
            # if theres a value at self.storage[index]
            # and curr.key == key , rewrite value
            curr.value = value
        else:
            # else if curr is None

            new = LinkedPair(key, value)
            # create room to be able to traverse there next
            # if mult keys for same bucket
            new.next = self.storage[index]
            self.storage[index] = new

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
        index = self._hash_mod(key)
        curr = self.storage[index]
        # will need prev to reorient pointers & del references to curr
        prev = None

        # if we're not deleting, we want to iterate through until we find curr.key=key
        while curr is not None and curr.key != key:
            # iterate
            prev = curr
            curr = curr.next

        if curr is None:
            print("key does not exist in storage")
            return None

        else:
            # if key found in storage:
            # delete the element by deleting its ref pointers in the LL
            if prev is None:
                # update storage[index] to equal curr.next (curr.next=None or just None) instead of curr
                self.storage[index] = curr.next
                # update curr to none
                curr = None
            else:
                # if prev is not None
                # delete prev's next reference to curr
                # instead of point prev.next ref to curr, point it to curr.next
                prev.next = curr.next

    def retrieve(self, key):  # O(1)
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        if self.storage[my_index] is None:
            return None
        else:
            return self.storage[my_index].contains(key)


Hash tables are O(1) average (insert, search,delete) and amortized case complexity, however it suffers from O(n) worst case time complexity. [And I think this is where your confusion is]

Hash tables suffer from O(n) worst time complexity due to two reasons:

1.If too many elements were hashed into the same key: looking inside this key may take O(n) time.
2.Once a hash table has passed its load balance - it has to rehash [create a new bigger table, and re-insert each element to the table].

However, it is said to be O(1) average and amortized case because:

1. It is very rare that many items will be hashed to the same key [if you chose a good hash function and you don't have too big load balance.
2. The rehash operation, which is O(n), can at most happen after n/2 ops, which are all assumed O(1): Thus when you sum the average time per op, you get : (n*O(1) + O(n)) / n) = O(1)   




        '''
        index = self._hash_mod(key)
        curr = self.storage[index]
        # iterate through the the LL at that bucket
        # loop through only if curr is not None & curr.key is not equal to key
        while curr is not None and curr.key != key:
            curr = curr.next

        if curr is None:
            print("key is not found")
            return None
        else:
            return curr.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        """
        # doubles capacity, change capacity since intiation of
        # HT takes capacity as ag to create self.storage
        self.capacity = self.capacity * 2
        doubled_storage = [None] * self.capacity
        # rehash k,v pairs
        # takes all indexes in new doubled self.storage
        for i in range(int(self.capacity/2)):
            # set values in new storage to values in self.storage[i]
            doubled_storage[i] = self.storage[i]

        # set self.storage to double_storage var
        self.storage = doubled_storage
        # for i in range(self.capacity):
        # create an extra space after every index position
        # self.storage.append(None)
        """

        temp_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for elem in temp_storage:
            if elem is not None:
                curr = elem

            while curr:
                # rehashes new key & inserts k,v
                # hash => returns hashed % self.capacity
                # since our capacity changed, our hashed index changes
                # self.insert rehashes our key, & puts it in the
                # corresponding indexes in our doubled capacity storage
                self.insert(curr.key, curr.value)
                # iterate through my next node
                curr = curr.next


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
