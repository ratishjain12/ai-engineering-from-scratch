## Static vs Dynamic Arrays

**Static Array**: A collection of data items stored in contiguous memory locations with a permanently fixed size determined at the time of creation.

**Dynamic Array**: A collection of data items stored in contiguous memory locations that automatically expands or shrinks its capacity during runtime as elements are added or removed

all native sequence types (like lists) in python are dynamic arrays under the hood, meaning they can automatically resize during runtime.

## Memory Allocation

Memory allocation determines how space is reserved in your computer's RAM.

**Static Arrays**: Space is allocated in a single, fixed-size contiguous block. This happens during compilation or object creation. The size cannot change

**Dynamic Arrays**: Space is also allocated in a contiguous block, but it starts small. When the block fills up, Python allocates a completely new, larger block of memory elsewhere. It copies the old data to the new block and frees the old memory.

## Random Access

Random access is the ability to read or write any item in an array instantly in O(1) constant time, regardless of its index position or the size of the array.

Both static and dynamic arrays support rapid random access because they store elements next to each other in sequence

Element Address = Base Address + (Index \* Element Size)
