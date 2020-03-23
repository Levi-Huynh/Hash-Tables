# Okay, remember, a hash table has two parts:
#  {
#   array: [None, None, None],
#   hashFunction: ()
# }
import time
​
# Our hash table needs to return an index in the array
​
# Let's make some toy functions!
​
length_of_array = 8
​


def myHash1(key):
    return len(key) % length_of_array


​
# Given dog, this returns the hash 3
​
# Pro:
# - deterministic
# - non-invertible, one-way function (if you know it gave back 3, do you know what key that belongs to?)
​
# Con:
# - output not unique! dog, dad, Tim
​
# We want the hash function to make hashes that are deterministic
# but LOOK random!
​
# Okay let's make it better


def myHash2(key):
    output_index = len(key) + time.time()


​
return output_index % length_of_array
# Pro:
# - non-invertible
# - pretty unique!
​
# Con:
# - not deterministic!! The time will always be different! acck!
​
​


def myHash3(key, salt):
    # this can also be add salt etc
    output_index = (len(key) * salt) % length_of_array


​
return output_index % length_of_array  # MODULO ENSURE INDEX IN OUR ARRAY!!!
# Pro:
# - deterministic
# - non-invertible
# - pretty unique!
​
# Con:
# - Gotta store the salt somewhere for this to be deterministic
​
​
# Okay, I also typed out djb2 during class, but it's a stretch goal!
# So I have removed it. However it's quite simple
# Rememer to use ord(char) inside your for-loop when you add the salt


def djb2(key):
    # some prime number
    our_salt = 5381

    # scramble each letter
    for char in key:
        hash_value = (our_salt << 5) + our_salt + \
            char  # scrambles errything up
    return hash_value


​
# djb2 is actually used, also check out:
# - sha256 - so unique, that never produced collision for 2 diff document , very secure. not too slow.
# some hash functions deliberately slow
# - bcrypt <-- deliberately slow. slows down hacking attempts to decode

# Calculate numbers by scrambling

# O(c) to access, and insert
# index to jump to where we want
# hash tables allows us to use strings not just index to look things up, and store things
# ^ HT extends power of arrays using indexes , allows us to store, access things using  strings, in constant time !!!
# print warning when overrite value, handle collision

#
