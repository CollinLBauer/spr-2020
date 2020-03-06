Collin Bauer

## HW6, part 2 - Locking

### c)

- flag.s ends with count = 26
  - flag.s uses a "flag" variable to determine if the critical section is "locked" before executing. However, setting this flag variable takes time before it registers, and since the program has no control over how many cycles it has before interrupting, it can't guarantee that this critical section will always be locked properly, leading to multiple programs thinking it is unlocked.

- test-and-set ends with count = 30
  - This is correct, but it's a little harder to reason out why. The operations look nearly identical to flag.s, except it uses the operator "xchg", which seems to swap two values, an operation that is not normally basic or fast.
  - It seems that the order which the lock check happens guarantees that when the jump happens, it will correctly read whether the section is locked.

- yield.s ends with count = 30
  - This version looks identical to test-and-set, except it uses and additional operator "yield", which seems to pause the execution of code to pass to another thread. It is therefore as correct as test-and-set, but a little bit faster, since it doesn't waste as many operations checking the lock.

### d)

- flag: 404 operations  
  test-and-set: 596 operations  
  yield: 560 operations

- Flag is easily the fastest, but its locking mechanism does not always work properly, which leads to some incorrect operations during the cirtical secion of code. Test-and-set locks properly, but wastes cycles checking if the lock is free. Yield does the same checking that test-and-set does, but will give up its operations to other threads if it sees that it is locked, leading to some saved cycles over test-and-set.

### e)

i.
- For flag, as the interrupt time gets smaller (more frequent), the count drastically reduces. As it gets bigger, the count (generally) gets more and more accurate. When the interrupt is an even multiple of the number of operations (11, 22), it guarantees count will be correct. Prime numbers (13, 17) also lend to greater inaccuracies.
- Test-and-set and yield are both accurate no matter the interupt.

ii.
- The number of operations all of them varies wildly with different values. Prime numbers lead to the largest run times for both flag and test-and-set. Yield does fine with prime numbers, but does not like small values, likely because yielding happens so often.