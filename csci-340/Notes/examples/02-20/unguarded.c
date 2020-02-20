#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int max;
volatile int counter = 0; //shared global variable

void *mythread(void *arg) {

    char *letter = arg;
    int i; // stack (private per thread)

    for (i = 0; i < max; i++){
        counter++;
    }
    printf("%s: done\n", letter);
    return NULL;
}

int main(int argc, char *argv[]){
    if (argc != 2){
        fprintf(stderr, "usage: main-first <loopcount>\n");
        exit(1);
    }
    max = atoi(argv[1]);

    printf("main: begin [counter = %d] [%p]\n", counter, &counter);
}