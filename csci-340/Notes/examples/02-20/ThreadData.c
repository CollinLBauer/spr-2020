#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int max;
volatile int counter = 0; // shared global variable

pthread_mutex_t lock;

typedef struct {
    int a;
    char *str;
} my_struct_t;

void *mythread(void *arg) {
    my_struct_t *mys = arg;

    printf("In thread fn, arg.c <%d>, arg.s <%s>\n", mys->a, mys->str);

    my_struct_t *rval = malloc(sizeof(my_struct_t));

    printf("In thread_fn rval adr<%p>\n", rval);

    rval->a = mys->a * 2;
    rval->str = "Returned String";

    return rval;
}

int main(int argc, char *argv[]){
    if (argc != 2){
        fprintf(stderr, "usage: main-first <loopcount>\n");
        exit(1);
    }
    max = atoi(argv[1]);

    printf("main: begin [counter = %d] [%p]\n", counter, &counter);

    my_struct_t vals = {max, "Bah Humbug"};

    // initialize lock
    assert(pthread_mutex_init(&lock, NULL) == 0);
}