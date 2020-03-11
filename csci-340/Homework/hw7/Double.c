// CSCI-340 - Homework #7

// Starter file for the double linked list


#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>


// basic node structure

typedef struct __node_t {
    
    int key;
    struct __node_t *next;
    struct __node_t *prev;

} node_t;

// basic list structure (one used per list)

typedef struct {
    
    node_t *head;
    node_t *tail;
    
} list_t;

// Initialize the list

void List_Init(list_t *L) {

    // Add code here to initialize the list
    
}

// Insert into the list (At the front)

void List_Insert(list_t *L,
                 int key) {

    // Add code here to safely insert a new node at the beginning of the list
    
}

// Insert into the list (At the end)

void List_Append(list_t *L,
                 int key) {

    // Add code here to safely insert a new node at the end of the list
    
}

int List_Lookup(list_t *L,
                int key) {

    // Add code here to lookup an item in the list
    
}

int main()
{

    // Add code here to test your list

    
}
