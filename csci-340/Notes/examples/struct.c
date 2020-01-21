// 01/16/2020
// in-class program
// struct.c
// Structure stample

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct myinfo {
    int field1;
    char field2[20];
    struct myinfo *next;

};

int main(int argc, char *argv[]){
    // create a linked list of structures

    struct myinfo *head = NULL;
    struct myinfo *mi_prev = NULL; // "intermediary" pointer, analagous to "curr" from 230?

    for (int i = 0; i < 10; i++){
        // Allocate and initialize a new element of the list
        struct myinfo *mi_new = malloc(sizeof(struct myinfo));
        mi_new -> field1 = i; // called referencing through
        mi_new -> field2[0] = (char)('A'+1);
        mi_new -> field2[1] = 0;
        mi_new -> next = NULL;

        // Attach the new node to the list
        if (head == NULL)
            head = mi_new;
        else
            mi_prev-> next = mi_new;
        
        // Save this nodes address
        mi_prev = mi_new;
    }

    // walk through the list

    struct myinfo *node = head; // pointer to head of the linked list

    while (node != NULL) {
        printf("(%p) field1 <%d>, field2 <%s>, next <%p>\n",
            node, node->field1, node->field2, node->next);
        node = node->next;
    }

    printf("Done.\n");
    return 0;
}
