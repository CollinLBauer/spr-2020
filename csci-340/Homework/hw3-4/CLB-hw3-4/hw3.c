#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[]) {
    char command[50];
    strcpy(command, argv[1]);
    for (int i = 0; i < argc - 1; i++) {
        strcat(command, argv[i+2]);
    }

    int status = system(command);
}