## Stack

A stack is a linear data structure that operates on the Last-In, First-Out (LIFO) principle. It acts like a real-world stack of plates, where the last plate added is the first one removed

**Key Operations**: Data is added or removed from the same end (the "top").

- Push: Adds a new element to the top.
- Pop: Removes and returns the top element.
- Peek: Views the top element without removing it.

#### Call Stack

A mechanism used by a computer program to keep track of execution of the code when calling multiple functions.

Key Purposes

- Tracks Execution: It remembers exactly where the program should return after a function finishes executing.
- Manages Memory: It allocates temporary memory for local variables created inside a function.

##### How it works

- Push: When a function is called, it is added to the top of the stack as a "stack frame."
- Execute: The program runs the code inside that top function.
- Pop: When the function finishes, its frame is removed from the top, and control returns to the previous function.

| Operation  | Time | Why                 |
| ---------- | ---- | ------------------- |
| push()     | O(1) | Append to end       |
| pop()      | O(1) | Remove from end     |
| peek()     | O(1) | Access last element |
| is_empty() | O(1) | Check length        |
| size()     | O(1) | Length lookup       |
