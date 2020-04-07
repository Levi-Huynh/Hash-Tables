No other data structures has O(1) for:

coveted: search, insertion, deletion 


Worst case ^ => O(n log(n)) 

why does worst case occur?

WHAT ARE HASH TABLES?
-Data Structure behind: 
    -Associate arrays & dictionaries 
    -Objects (Python, Javascript, ruby) called dicts in python 
    -Caches (Memcached)
    -Dynamic Programming, Memoization 


-Key/Value data storage & retrieval:
    -Data is stored in a contiguous block of memory as an array 
    -Key is converted to an integer vai a hash function  
    -Hashed key is converted to an array index via modulo function 


hash_table[Key] = Value;

//Pseudocode 
// int index = hash_function(Key) % array.length; 
//array[index] = Value 


What is a _Hash_ Function? 

# One way mapping from arbitrary data to fixed data size & type 

# Many different hash functions with different attributes:
    -Deterministic # If input & hash function remains the same, the output gibberish string created always the same
    -Uniform Distribution #  input close to another input will be on average very far away from original input 
    -Non-invertible #can't take result hashed output to figure out the input/original pw
    -Continuous vs non-continuous #similar to distribution 

    #diff hash functions have diff use cases


What is a Hash Function? 

// Sums the ascii values of the characters in a string & returns a modul 
// string -> integer (0, 31)

int basic_string_hash(char str[]) {
{
    int hash = 0;
    for(int i=0; str[i]!= '\0'; i ++) {
        hash += str[i];
    }
    return has % 32; 

}

}


basic_string_hash("hello");

//['H', 'e', 'l', 'l', 'o'] => [72, 101, 108, 108, 111] -> 500
//500 % 32 = 20 

-turn input key in array index
-since our array is size 32, we want that to be between 0 & 31 


# How Do Hash Tables work? 

1) Declare an empty array
    -Power of 2 (32) (usually)
    -arr = malloc(Default_SIZE *sizeof(VALUE_TYPE)) *sizeof(Int) for example 
2) Hash the Key
    -basic_string_has("Hello")-> 20 
3) Assign Value to hash index 
    -arr[20] = Value; 


# HASH COLLISION & RESIZING 

- 2  Keys Hash to the same Index 
    -Hash just created, take key, runs through hash function => generates an index in array 
    -underhood hash is array. 
    -2 key hashed to same index == collision!

bday problem
    pidgeon hole problem: probably reaches 100% when the number of ppl reaches 367 (since 366 bdays including feb 29) that there will 2 ppl w/ same bday.  
    
    W/ HASH TABLE? 99.9% probability reached w/ 70 ppl & 50% probability with 23 ppl  

    collision: 1-k!/ ((k-n)! * k ^n)) 
    takeway: collisions are unavoidalbe 

    handling collisions
    Many different methods:
        -open addressing
            -when collision, looks at neighbors to see if there are open spots to filled
        -linked list chaining: 
            -most convetional method
            # elemnents in HT are stored as LL
                -store the value, key, and pointer to next value in chain 
            # when retrieiving a value, traverse down the linked list until you find the matching key 
            # HT method still applies, Ex below is __inserting__ 
                -take key
                -insert key into hash function 
                -generate index of array
                -traverse down to see if that key matches, if matches: overwrite value 
                -insert at end, if next pointer is null & _key_ doesn't match
                -^ delete/searching similar
        

# LL CHAINING PERFORMANCE 
    Time complexity
    -insert, delete, search for LL are O(n), O(1) for HT 
        -(worst case for HT if all hashed indexes are same, will have to go thru each elemeent n times: n log n) 
    Space Complexity:
    -__Must store key, value & pointer for each hash table etnry__
    -Lots of Empty slots
    -still O(n)

# DEGRADATION PERFORMANCE, HASH TABLE RESIZING 
    -Load factor = (number of entries)/(hash table capacity) #more elements that u need to traverse, closer to O(n)
    -when load factor passes a certain threshold, resizing can occur
        -create a new has table table with double capacity 
        -copy elements from the old hash talbe to the new one / one at a time
        -resizing is O(n) BUT occurs at O(log n) frequency 


For Basic HT with no collision handling:
If every single slot in HT is occupied, max load capacity is 1 

LL can have multiple elements in each slot, so max load capacity can be >1

The longer LL gets, the worse the performace of HT gets

^ High level lang test:
-check everytime insert, when load factor pases thresh of .07 
will resize entire hash table
-creates copy empty HT, of size DOUBLE of original HT, and copy each element over at time
-each key rehased, move over to doubled HT, removed from original 
- size down, for HT, for very large HT where moemory is concerned 

reisze is O(n) but occurs at O(log n) frequency 

since ocurs at log n decline freq

HT of size 128, run resize op every time have 129 (load factor 1)
run only 256 inserts, reize to 512, 1,024, 2048, gives us it still avgs out to constant time insert 

functional HT:
-collision handling 
any amount of inputs, still has O(1)

Hash tables are O(1) average (INSERT, SEARCH, DELETE) and amortized case complexity, however it suffers from O(n) worst case time complexity. [And I think this is where your confusion is]

Hash tables suffer from O(n) worst time complexity due to two reasons:

1.If too many elements were hashed into the same key: looking inside this key may take O(n) time.
2.Once a hash table has passed its load balance - it has to rehash [create a new bigger table, and re-insert each element to the table].

However, it is said to be O(1) average and amortized case because:

1. It is very rare that many items will be hashed to the same key [if you chose a good hash function and you don't have too big load balance.
2. The rehash operation, which is O(n), can at most happen after n/2 ops, which are all assumed O(1): Thus when you sum the average time per op, you get : (n*O(1) + O(n)) / n) = O(1)   