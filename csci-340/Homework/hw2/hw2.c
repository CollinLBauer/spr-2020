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
