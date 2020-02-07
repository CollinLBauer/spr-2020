#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main(int argc, char *argv[]) {
    // check if program is run with arguments
    if (argc <= 1){
        printf("Arguments expected.\n");
        return -1;
    }
    char command[50];                   // declare command size
    strcpy(command, argv[1]);           // copy first command
    for (int i = 2; i < argc; i++) {    
        strcat(command, " ");
        strcat(command, argv[i]);       // copy additional commands
    }

    int pid = fork();
    if (pid == 0){
        printf("I am the child.\n");
    }
    else{
        printf("I am the parent.\n");
        printf("The child pid is: %d\n", pid);
    }

    /*
    int status = system(command);       // system call for commands
    return status;
    */
}