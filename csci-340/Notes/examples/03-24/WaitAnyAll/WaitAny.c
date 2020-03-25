// Waiting for any of multiple threads

#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void thr_signal(int i) {

}

void thr_wait(int *who_signaled) {

}

void *child(void *arg) {

    int whoami = (long)arg;

    // Sleep for some random amount of time
    int to_sleep = rand() % 5;
    printf("Child %d: Start, sleeping %d\n", whoami, to_sleep);
    sleep(to_sleep);

    // Signal completion
    thr_signal(whoami);
    printf("Child %d: After Signal\n", whoami);
    
    return NULL;
    
}

int main(int argc, char *argv[]) {
    
    printf("Parent: Start\n");

    if (argc != 2) {
        printf("Usage: WaitAny n_threads\n");
        exit(13);
    }

    // Seed the random generator
    srand(time(NULL));
    
    printf("Parent: End\n");
    
    return 0;
}
