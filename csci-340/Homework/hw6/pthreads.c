#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

struct threadParams{
    int threadnum;      // number of the current thread
    int strLen;         // length of the string
    char *string;       // pointer to the string
    int *curr;          // pointer to string current position
};

void *threadFun(void *args){
    struct threadParams *data = args;
    printf("Thread: %d: %c\n", data->threadnum, (char)data->threadnum + 65);

    while (*data->curr < data->strLen){
        data->string[*data->curr] = data->threadnum + 65;
        *data->curr += 1;
    }
    free(args);
    return NULL;
}

int main(int argc, char **argv){
    if (argc != 3){ // assert arguments
        printf("%d arguments found; expected %d.", argc-1, 2);
        printf("Usage: ./pthreads <thread-num> <len-string>\n");
        exit(1);
    }
    printf("Starting...\n");

    // grab command line arguments
    int numThreads = atoi(argv[1]);
    int strLen = atoi(argv[2]);

    // instantiate empty string
    char *finalString = malloc(strLen * sizeof(char));
    memset(finalString, 0, strLen * sizeof(char));

    //malloc threads
    pthread_t *threads = malloc(numThreads * sizeof(pthread_t));
    
    // counts the length of the string
    int curr = 0;
    int *curr_ptr = &curr;

    // Create threads
    for (int i = 0; i < numThreads; i++){
        // parameters
        struct threadParams *params = malloc(sizeof(struct threadParams));
        params->threadnum = i;
        params->string = finalString;
        params->strLen = strLen;
        params->curr = curr_ptr;

        pthread_create(&threads[i], NULL, *threadFun, (void*)params);
    }
    for (int i = 0; i < numThreads; i++){
        pthread_join(threads[i], NULL);
    }
    printf("After...\n"); //debug
    
    printf("Final string: [%s]\n", finalString);

    // clear memory and end program
    free(finalString);
    printf("Done\n");
    exit(0);
}
