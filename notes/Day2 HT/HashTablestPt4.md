# Names example from the sprint

# Creating a dictionary instead of using the nested for loops, allows us to loop through only once 

# dicionaries, objects are hash tables under the hood, but with different syntactic sugar . HT more of a language agnostic principles applicable to most high level lang

# good to use CS terminology in interviews..

# HT COLLISIONS

-overwrite previous Key value pairs

-more than one k,v in same index

-1 solution:
    -create Linked list node, store key, value there
    - each k,v w/ same index, create a new node

    -when searchnig for key in hash function, & come to 
    an index w/ multiple nodes (search thru the LL node to see if key matches, return value if match)

    -head of LL is the first k,v, etc...

    -handle collision, continue to append to head or to tail, depending on which you have pointer to /how LL is implemented 

    -searching LL is O(n)

    -collisions cause more nodes to be created, changing the access at certain indexes from O(c) to O(n)

    -Bday/ repeat indexes probability greater than you think!  