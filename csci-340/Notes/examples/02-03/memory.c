#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    /* aoti converts strings to integers
     * if a string is not an integer, returns 0
     */
    int len = atoi(argv[1]);
    char *string_mem = malloc(len);
    
    printf("%d: Code address <%p>\n", len, &main);
    printf("%d: Stack address <%p>\n", len, &len);
    printf("%d: Heap address <%p>\n", len, string_mem);

    free(string_mem);
    return 0;
}