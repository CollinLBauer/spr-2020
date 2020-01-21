// Collin Bauer
// I'm still trying to figure out what to do here.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <memory.h>


// Doubly linked list of process IDs
struct pidElement {
    int pid;
    struct pidElement *prev;
    struct pidElement *next;

};

int main(int argc, char *argv[]){
    if (argc <= 1) {
        printf("Requires one positional argument.\n");
        return 0;
    }
    
    int var = atoi(argv[1]);
    printf("argv[1] <%d>\n", var);
    //malloc(&argv[1]);

    return 0;
}
