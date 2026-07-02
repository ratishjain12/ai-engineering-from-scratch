## Queues

A linear data structure that operates on the First In, First Out (FIFO) principle, meaning the first element added to the queue will be the first one to be removed.

Primary Operations
All core operations typically achieve a time complexity of \(O(1)\).

- enqueue(): Adds an element to the rear of the queue.
- dequeue(): Removes and returns the element from the front of the queue.
- peek() / front(): Returns the front element without removing it.
- isEmpty(): Checks if the queue contains no elements.
- isFull(): Checks if a fixed-size queue has reached its maximum capacity.

Types of Queues

- Simple Queue: Linear structure following strict FIFO ordering.
- Circular Queue: The last position connects back to the first, optimizing space by reusing vacated memory slots.
- Priority Queue: Elements are pulled out based on an assigned priority rather than strictly their arrival order.
- Double-Ended Queue (Deque): Allows insertion and deletion from both the front and rear ends
