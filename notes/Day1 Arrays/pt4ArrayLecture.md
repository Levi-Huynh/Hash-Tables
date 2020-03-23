Python dicts have extra helper methods 

object/
hash map/
dict

made up of:

{ array: [], HashFunction: f()}  //dynamically sized arr, //several flavors of f()}

how are arrays stored in memory:

5000 5004 5008 5012  5016 

1     2    3   4      5

RAM/memory, store in memory cells (5000, 5004) 
# Creating new Array
1) program asks computer for memory (not allowed to write to mem directly)
2) mem. the OS gives you is all next to each other (for arrays, contiguous, sequential.)
    #if want 4th bucket, get index of that bucket, bucket size 4, index 3, 
        # 3 (indexOfbucket) * 4 (bucket/value) + startMemAddress(5000) = 5012 __memory-address__ 
        or memory_address + numberOfBits 
        #also depends on how many bytes/what is being stored in each memory ram cell, if its 1:1 for the value & cell
        #8 bits is a byte 
        #half a byte is a nibble 
3) gives you a completely new memory address, with sometimes double space you requested #the extra space given will double by lang 
#question first time your request /create array are you given the _exact_ amount of mem cells. Only given extra memory cells after the first request? 
4) copy each element over one at a time (resizing) => O(n)

# Inserting to array
1) if array already exists, but memory cells not all filled
2) want to insert in between 2 values/buckets
3) pick up all the elments to right of where you want to insert, & move it over 1 (as long as their memory cells available at ends to the right) #do this by copying each element, set it to right & overwrite whats there 
4) inserting into middle array: RT: O(n), have to move each array to the right, over one 
#remember this hopscotch, move each over 1 to right of ops, wil help

# Dyanmic Array: resizes when needs to
see dynamicArraypt4.py

# We need _deterministic_ hash functions: 
    need HF f() thats deterministic, if given smame string, / key, always get the same back the same index 

# review

# searching array O(n)
# accessing array O(c)
# creating/ storing key value pair O(c)
# reading from hash table O(c)
    -b/c don't have to traverse, just plug key 
    into hash, get index, access array w/ index givne from hash function is O(c)