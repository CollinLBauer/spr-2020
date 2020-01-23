// work with sizeof

#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    char *x = NULL;
    printf("size of char *<%ld>\n", sizeof(x));

    x = malloc(10);
    printf("size of what x points to <%ld>\n", sizeof(*x));

    int int_array_size = sizeof(int) * 10;
    int *int_array = malloc(int_array_size);

    for (int i = 0; i < 10; i++){
        int_array[i] = i;
    }

    printf("int_aray_size <%d>\n", int_array_size);
    printf("int_array_pointer <%p>\n", int_array);
    printf("int_array[2] <%d> <%p>\n", int_array[2], &int_array[2]);


    return 0;
}