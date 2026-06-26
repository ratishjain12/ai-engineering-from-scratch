## Context Managers

tools that automatically allocate and release external resources precisely when you need them

They are typically invoked using the **with** statement, which guarantees that clean-up code runs smoothly even if your program encounters errors or crashes mid-execution

### Why Use Context Managers?

**Prevent Resource Leaks**: Keeps file streams, database connections, and network sockets from locking up.

**Cleaner Syntax**: Replaces ugly, repetitive try...except...finally blocks with an elegant, readable structure.

**Safe Error Handling**: Guarantees teardown logic finishes executing even when unexpected runtime crashes happen
