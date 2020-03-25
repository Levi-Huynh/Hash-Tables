import random
​


def how_many_before_collision(loops, length_of_array):


​
for i in range(loops):
    tries = 0
    tried = set()
    while True:
        random_key = random.random()  # prints random num between 0 & 1 (like cat, dog key)
        hash_index = hash(random_key) % length_of_array
        if hash_index not in tried:
            tried.add(hash_index)
            tries += 1
        else:
            break
    print("we had {} buckets, and {} hashes before collision".format(
        length_of_array, tries))
​
# ^ more memory, will still have fewer collisions, BUT collisions still __occur__
# if we know how many time we get the _same_ index will tell us the length of our LL
# at that index (things will keep getting stored there)

# for storing k,v in class Node
# self.value = tuple (which has  key, value pair stored together) (key, value)
# self.value = ('dog', 'bark')
# must store both k,v

# several ways to update /edit non editable node:
# remove, then add new node
# just update the value, by setting a new tuple!

# ----------------------------------------------------------
# hwk hints:
# insert always create LL easier to work
