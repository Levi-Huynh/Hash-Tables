Objectives:
1) understand memory structure of an array
2) understand how inserting into an array works
3) Know the diff between arrays & Python lists  

1) array:
    Seq of elements of the same type, stored in a contiguous block of memory

How to declare array?
1) determine how big the array needs to be 
2) request a block of memory that will fit the array 
3) recieve the memory address of the reserved block
4) write your values into memory

Declare the array: [2,3,4,5]

1. determine how big the array needs to be
    - `an integer is 4-bytes so the array needs to be 16-bytes`
    - `byte consists of 4 bits, bit is either 1 or 0`
2. Request a block of memory that will fit the array    
    - `rquest 16-bytes of memory from the computer`
3. Recieve the memory address of the reserved block 
    -`recieve an address to the start of the 16-bytes of reserved memory`
4. Write your values into the array 

Declare array: [2,3,4,5]
//request this much memory
// to acess  `memory address` of an index in the array:
// `index * sizeof(type) + start_address` (peack efficiency requires us to start from 0 index )

//25600 is memory address, doesnt matter as much, doest always start at begining 

25600       25601       25602        25603 
00000000    00000000    00000000    00000010    //2

25604         25605       25606        25607 
00000000    00000000    00000000    00000011    //3

25608       25609       25610        25611 
00000000    00000000    00000000    00000100    //4

25612         25613       25614        25615 
00000000    00000000    00000000    00000101    //5

//index 
// how to find address of 3rd element:
// index = 2, * size of our type (in this case int) = 4, + start address =25600  == 25608 == addres of 3rd element 

//very fast operations 
//accessing index of area, O(1) quantaum speed
//very space effecient too (packed like sardines)

//each element must be the same type 
//sequential
//continuous block of memory

//add element to end of array 
1. take size of current array & increase it by one element 
2. Req a block of memory of the new size (if 4 bytes/int, array of 5 int=20bytes, array 4 int=16 bytes)
3. Copy each element from old space to the new space one byte at a time // this is the SLOW PART! 
    -kind of like the swap space 
4. free the memory from the old array 
    -This is an O(n) operation 
    -the old specific sized 16 block of memory for array of 4 int, is now not being used. Leads to 
    `fragmentation` . Little tiny memory slots that can only store specifically 4 integers.


HOW DOES _PYTHON_ ADD AN ELEMENT TO THE END OF THE LIST?
-Python will allocate a few __extra__ empty spaces each time the array grows 
-Each time your list grows, it allocate a bit more extra space than previous (maybe 4, 8, 9 , 10 etc)
-^ less need to copy over everything one element of time to new space 
-if don't have to do all of them one by one: rt: O(1) . Ptyhon add usually considered O(1)
-if have to copy all elements one by one : O(n) sometimes 
- on average adding is O(1

-Ok to assume, as frequency of adding occurs, more likely to be an O(1) rt?? 
-can't gaurantee when wil get slow/fast operation though!!! 

HOW DOES PYTHON ADD AN ELEMENT TO THE begining OF A LIST?
1. Check if theres any empty space at the end of the array 
2.  If not: 
    1) allocate a new array, pace the first lement and copy over the test
    2) Free memory from the old array 
3 If so: 
    1) starting at back, move Each element to the right one space 
    2) Place new element in first position 
    O(n) operation no matter what for insert into front!!! :) 

    
    #code test compare rt of adding to the front (using insert(index), & append(), which adds to back)

insert code, which inserts to front creates O(n^2) to account for for loop in code, & the insert to front of list operation that 
occurs under the hood 

add to back is O(n)

Add to back was 600x faster than ad to front! LOL 0.08 secs verssus 50.61 secs <<< why know Big O is important!

ARRAYS ARE EXTREMELY TIME & SPACE EFFICIENT NO WASTE
    -EXCEPT: WASTE/SNIPPETS OF UNUSED ALLOCATED memory

PYTHON LISTS TAKE CARE OF SIMPLE OPS FOR YOU 
    - BUT ITS NOT MAGIC 

-UNDERSTAND ARRAYS HELP YOUR CODE TO BE MUCH MORE EFFICIENT 


