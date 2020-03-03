#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

struct threadParams{
    int threadnum;
    char *string;
    int strLen;
};

void *threadFun(void *args){
    struct threadParams *data = args;
    int i = 0;
    char val[10] = {};

    printf("  In thread %d\n", data->threadnum);

    while (i < data->strLen){
        printf("%d\n",i);
        printf("[%s]\n",data->string);
        sprintf(val, "%d", i);
        printf("hi\n");
        data->string[i] = val[0];
        i++;
    }
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

    // placeholder
    int i = 0;

    // parameters     
    struct threadParams *params = malloc(sizeof(struct threadParams));
    params->threadnum = i;
    params->string = finalString;
    params->strLen = strLen;

    // run threads
    printf("Before thread...\n");
    pthread_create(&threads[i], NULL, *threadFun, (void*)params);
    pthread_join(threads[i], NULL);
    printf("After thread...\n");
    
    printf("Final string: [%s]\n", finalString);

    // clear memory and end program
    free(finalString);
    printf("Done\n");
    exit(0);
}
