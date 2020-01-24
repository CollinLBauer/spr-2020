Collin Bauer

CSCI 340 - Operating Systems

## Homework 2

---

### Parts 1 and 2

**Code from assignment**

```
// Collin Bauer
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <memory.h>

/* Part 1 - Lists and Structures*/

// process context structure
struct process {
    int pid;                // process ID

    // context
    char *inst;             // instruction pointer
    char *stack;            // stack pointer
    int AX;                 // register
    int BX;                 // register

};

// process node for Doubly Linked List
struct process_node {
    struct process proc;

    struct process_node *prev;
    struct process_node *next;
};

// process state enumerator
enum proc_state{ INITIALIZING, RUNNING,
                 SUSPENDED, READY, TERMINATED };


/* Part 2 - C Pointers and References */
int main(int argc, char *argv[]){
    if (argc <= 1) {
        printf("Requires one positional argument.\n");
        return 0;
    }
    
    // create memory allocation
    int size = atoi(argv[1]);
    int *stored = malloc(size * sizeof(int));

//    printf("size: %d\n", size); //debug
    printf("stored <%p>\n", stored);

    // set each byte to 0
    memset(stored, 0, size * sizeof(int));

    // iterate over and print eachmemory address
    for (int i = 0; i < size; i++){
        printf("stored[%d]: 0x%x\n", i, stored[i]);
    }
    
    // free memory and end execution
    free(stored);
    printf("Done.\n");
    return 0;
}

```

**Example output**

```
stored <0x559c2487c260>
stored[0]: 0x0
stored[1]: 0x0
stored[2]: 0x0
stored[3]: 0x0
stored[4]: 0x0
stored[5]: 0x0
stored[6]: 0x0
stored[7]: 0x0
stored[8]: 0x0
stored[9]: 0x0
stored[10]: 0x0
stored[11]: 0x0
stored[12]: 0x0
stored[13]: 0x0
stored[14]: 0x0
stored[15]: 0x0
stored[16]: 0x0
stored[17]: 0x0
stored[18]: 0x0
stored[19]: 0x0
Done.
```

---

### Part3 - Process Transitions

**Ready**
- Running - If a process is waiting to run, the task scheduler may tell it to start (or continue) running.
- Suspended - If another process needs to take priority according to the task scheduler, the process may be stored into memory and suspended for the higher priority process.
- Terminated - A process may be forcibly terminated from any state.

**Suspended**
- Ready - If a process is suspended and exists in memory, it may be loaded by the operating system and resume execution at any point. Note that it doesn't immediately go into the "running" state.
- Terminated - A process may be forcibly terminated from any state.

**Running**
- Suspended - The task scheduler may tell a running process to "suspend" its execution so other processes may take priority; its data is then stored away in memory to be called later.
- Ready - If a process is sharing CPU usage with others, it may swap between "running" and "ready" states so resources may be shared properly.
- Terminated - If the process has finished execuiting, it has no reason to exist anymore and may be safely terminated.

---

### Part 4 - Scheduling Policies

***CFS***

The Completely Fair Scheduler (CFS) is an implementation of so-called "fair share" scheduling, where each process gets a proportional percentage of the CPU time. It is extremely efficient (and therefor fast) thanks to clever use of data structures. As more processes are added, it decreases the size of a time slice, so CPU usage spreads out more. However, there is also a minimum time slice size specified (minimum granularity), so the CPU doesn't spend too much time switching processes.

<br/>

***BFS***

The Brain **** Scheduler (BFS) is another fair scheduler that attempts to keep a simple approach to its slice-sharing algorithms. It uses a single queue (structured as adoubly-linked-list) for all processes. In contrast to CFS, all tasks use the same sized time slice, with the exception of realtime tasks of the highest priority, which have "infinite" time slices.
