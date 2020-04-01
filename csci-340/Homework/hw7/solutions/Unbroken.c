#include <assert.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct __node_t {    
    int               value;
    struct __node_t * next;
} node_t;


typedef struct {    
    node_t *        head;
    node_t *        tail;
    pthread_mutex_t head_lock;
    pthread_mutex_t tail_lock;
} queue_t;


void Queue_Init(queue_t *q) {
    node_t *tmp = malloc(sizeof(node_t));
    tmp->next = NULL;
    q->head = q->tail = tmp;

    pthread_mutex_init(&q->head_lock, NULL);
    pthread_mutex_init(&q->tail_lock, NULL);
}


void Queue_Enqueue(queue_t *q, int value) {
    pthread_mutex_lock(&q->tail_lock);
    node_t *tmp = malloc(sizeof(node_t));         /* Get a new node */
    if (tmp == NULL) {                            /* Did the allocation fail? */
        perror("malloc");
        return;
    }

    assert(tmp != NULL);
    tmp->value = value;                           /* Set the node's contents */
    tmp->next  = NULL;                            /* Show it's the tail */

    q->tail->next = tmp;                          /* Point old tail to new tail */
    q->tail = tmp;                                /* Point tail to new node */

    pthread_mutex_unlock(&q->tail_lock);
}


int Queue_Dequeue(queue_t *q, int *value) {
    // Failure is always an option
    int rc = -1;

    if (q->head->next != NULL) {
        *value = q->head->next->value;            /* Return the value */
        printf("  In if\n");
        pthread_mutex_lock(&q->head_lock);        /* Lock the list */
        node_t *tmp = q->head;                    /* Save the old head node pointer */
        q->head = q->head->next;                  /* Reset the head */
        pthread_mutex_unlock(&q->head_lock);      /* Unlock the list */
        free(tmp);                                /* Free the old head node */
        rc = 0;
    }
    return rc;
}


/* main for testing purposes */
int main(int argc, char **argv){
    queue_t *myQueue = malloc(sizeof(queue_t));
    Queue_Init(myQueue);


    for (int i = 10; i <= 100; i += 10){
        printf("%d\n", i);
        // add some values to queue
        Queue_Enqueue(myQueue, i);
    }

    int *rtnVal = 0;
    node_t *tempHead;
    while (myQueue->head != NULL){
        // dequeue every entry in queue
        tempHead = myQueue->head;
        Queue_Dequeue(myQueue, rtnVal);
        printf("In while\n");
        printf("Node <%p>\nVal: %d\n\n", tempHead, *rtnVal);
    }

    printf("Done.\n");
    exit(0);
}
