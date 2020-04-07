"""
Amortized time looks at an algorithm from the viewpoint of total running time rather than individual operations. 
We don't care how long one insert takes, but rather the average time of all the calls to insert 

In terms of amortized time, append RT is pretty constant O(c), except when have to resize..resize rt is O(n)
but without that once in a while op of resize, append is O(c)
"""


class DynamicArray:  # AUTO RESIZES FOR US!
    def __init__(self, size):
        self.count = 0
        self.size = size


​
# will create empty array of whatever the size you want
self.storage = [None] * size  # reservering space
# ^heres our array we'll be manipulating & working with
# ex: ['hello'] * size ==> create array with hello, size times
​
# [None, None, None, None]
# value: 1
​


def append(self, value):  # ADDS TO END OF ARRAY O(1) (no shifts, unless must resize)
    if self.count == self.size:
        self.resize()  # O(n) shifts item & copies 1 by 1


​
self.storage[self.count] = value
# self.count started at zero, add 1 to iterate index, each time self.storage[self.count] intializes new value,
self.count += 1
​
# [1, 2, 2, 3, 4]


def insert(self, value, idx):  # ADDS AT INDEX O(n)
    # check if enough capacity, resize/add capacity if we need
    # each value has address
    # arrays and lists are dynamic
    if self.count == self.size:
        self.resize()


​
# move everything over by one
# start at the last element in arr (self.count), stop back at index, decrease by 1
# O(n)
for i in range(self.count, idx, -1):
    # start from back, copy prev value to the back, copy next prev to next back lot etc
    # swap storage[i] with previous storage[i-1] iterate backwards
    self.storage[i] = self.storage[i - 1]
​
# add new value to index
self.storage[idx] = value
​
self.count += 1
​


def resize(self):
    # double size
    self.size = self.size * 2


​
# make a new array, which is double the size of the old array
# [None, None, None, None, None, None, None, None]
temp_storage = [None] * self.size
​
# copy everything into the new array
for idx in range(self.size / 2):  # can also use self.count #idx goes from 0=>9
    # SELF.STORAGE IS THE MAIN ITEM UR ITERATING HERE, TEMP_STORAGE IS JUST THE VAR YOUR STORING THESE VALUES TO!
    temp_storage[idx] = self.storage[idx]
    # iterates thru the old self.size range (before doubled)
    # , sets self_storag[@ indx] to temp var temp_storage[index]
    # old storage from append/insert
​
self.storage = temp_storage

# is preallocating faster than appending?
#


"""
{
        
}
"""
