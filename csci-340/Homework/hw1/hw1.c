#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    printf("argc: %d\n\n", argc);
    int argLength = sizeof(&argv) / sizeof(&argv[0]);
    for (int i = 0; i < argc; i++){
        printf("%d: %p\n", i, &argv[i]);
    }
    printf("\nDone.\n");
    return 0;
}