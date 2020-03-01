#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int main(int argc, int *argv){
    if (argv != 1){
        printf("%d arguments found; expected %d.", argc, 2);
        printf("Usage: ./pthreads <thread-num> <len-string>\n");
        exit(1);
    }
    int numThreads = argv[0];
    int strLen = argv[1];


    exit(0);
}
