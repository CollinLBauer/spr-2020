#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int max;
volatile int counter = 0; //shared global variable

pthread_mutex_t lock; // special struct; acts as thread locker

void *mythread(void *arg) {

    char *letter = arg;
    int i; // stack (private per thread)

    for (i = 0; i < max; i++){
        /* critical code section
         * one thread will wait for the other
         * to finish this before attempting its own
         */
        assert(pthread_mutex_lock(&lock) == 0);
        counter++;
        assert(pthread_mutex_unlock(&lock) == 0);
        // end of critical section
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

    // initialize lock
    assert(pthread_mutex_init(&lock, NULL) == 0);
}