#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *threadFun(int *threadNum){
    //TODO
    printf("In thread %d\n", *threadNum);
    return NULL;
}

int main(int argc, char **argv){
    if (argc != 3){
        printf("%d arguments found; expected %d.", argc-1, 2);
        printf("Usage: ./pthreads <thread-num> <len-string>\n");
        exit(1);
    }

    int numThreads = atoi(argv[1]);
    //int strLen = atoi(argv[2]);

    pthread_t *threads = malloc(numThreads * sizeof(pthread_t));
    for (int i = 0; i < numThreads; i++){
        printf("Starting thread %d...\n", i);
        pthread_create(&threads[i], NULL, *threadFun, &i);
    }

    printf("Done\n");
    exit(0);
}
