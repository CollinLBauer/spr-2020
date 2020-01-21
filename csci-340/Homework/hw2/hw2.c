// Collin Bauer
// I'm still trying to figure out what to do here.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <memory.h>


// Doubly linked list of processes
struct pidElement {
    // element contents
    int pid;                // process ID

    int AX;                 // register
    int BX;                 // register
    
    // pointers to other elements
    struct pidElement *prev;
    struct pidElement *next;

};

int main(int argc, char *argv[]){
    if (argc <= 1) {
        printf("Requires one positional argument.\n");
        return 0;
    }
    
    int size = atoi(argv[1]);
    int *stored = malloc(size * sizeof(int));
//    printf("size <%d>\n", size); //debug
    printf("stored <%p>\n", stored);
    
/*    
    // print before memset
    printf("Before memset()\n");
    for (int i = 0; i < size; i++){
        printf("stored[%d]: %d\n", i, stored[i]);
    }
*/

    memset(stored, 0, size * sizeof(int));
    for (int i = 0; i < size; i++){
        printf("stored[%d]: 0x%x\n", i, stored[i]);
    }
    
    free(stored);
    printf("Done.\n");
    return 0;
}
