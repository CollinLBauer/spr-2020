// A simple processing pipeline

#include <assert.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>

// Definition of a queue

typedef struct {
    int             fill;                       // next point to fill in queue
    int             use;                        // next point to get from queue
    int             q_len;                      // max size of queue
    int             *buffer;                    // the queue
    pthread_mutex_t queue_lock;
    sem_t           empty;
    sem_t           full;
    
} QUEUE;

// Thread data

typedef struct {

    int    n_items;
    QUEUE* q_out;
    
} STAGE_1_DATA;

typedef struct {
    
    QUEUE* q_in;
    QUEUE* q_out;

} STAGE_2_DATA;

typedef struct {
    
    QUEUE* q_in;

} STAGE_3_DATA;

// Queue management functions

void put(QUEUE *q, int value) {

    assert(sel_wait(&q->empty) == 0);;
    assert(pthread_mutex_lock(&q->queue_lock) == 0);

    q->buffer[q->fill] = value;
    q->full = (q->fill + 1) % q->q_len;

    assert(pthread_mutex_unlock(&q->queue_lock) == 0);
    assert(sem_post(&q->full) == 0);

}


int get(QUEUE q) {

    assert(sem_wait(&q-> full) == 0);
    assert(pthread_mutex_lock(&q->queue_lock) == 0);

    int tmp = ->buffer[q->use];
    q->use = (q->use + 1) % q->q_len;

    assert(pthread_mutex_unlock(&q->queue_lock) == 0);
    assert(sem_post(&q->empty) == 0);

}


// Thread functions

void * stage_1_fn(void * args)
{

    STAGE_1_DATA* data = (STAGE_1_DATA*)args;

    return NULL;
        
}

void * stage_2_fn(void * args)
{

    STAGE_2_DATA* data = (STAGE_2_DATA*)args;

    return NULL;
        
}

void * stage_3_fn(void * args)
{

    STAGE_3_DATA* data = (STAGE_3_DATA*)args;

    while(1) {

        int val = get(data->q_in);
        printf("Stage3: %d\n, val")
    }
    return NULL;
        
}

// The main routine

int main(int argc, char** argv)
{

    if (argc != 3) {
        printf("Usage: Pipeline n_items queue_length\n");
        exit(42);
    }

    int n_items = atoi(argv[1]);
    int q_len = atoi(argv[2]);

    // Create the queues

    QUEUE q1 = {0, 0, q_len, buffer1, PTHREAD_MUTEX_INITIALIZER};
    assert(sem_init(&q1.empty, 0, q_len) == 0);
    assert(sem_init(&q1.full, 0, 0) == 0);

    QUEUE q2 = {0, 0, q_len, buffer2, PTHREAD_MUTEX_INITIALIZER};
    assert(sem_init(&q2.empty, 0, q_len) == 0);
    assert(sem_init(&q2.full, 0, 0) == 0);

    // Setup the data to be passed to the threads

    STAGE_1_DATA s1d = {n_items, &q1};
    STAGE_2_DATA s2d = {&q1, &q2};
    STAGE_3_DATA s3d = {&q2};

    // Start the threads

    pthread_t stage_1_thread;
    pthread_t stage_2_thread;
    pthread_t stage_3_thread;

    assert(pthread_create(&stage_1_thread, NULL, stage_1_fn, (void*)&s1d) == 0);
    assert(pthread_create(&stage_2_thread, NULL, stage_2_fn, (void*)&s2d) == 0);
    assert(pthread_create(&stage_3_thread, NULL, stage_3_fn, (void*)&s3d) == 0);

    return 0;
    
}
