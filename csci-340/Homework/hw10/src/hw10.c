#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <memory.h>

int main(int argc, char **argv) {
    // assert usage
    if (argc != 2){
        fprintf(stderr, "Usage: ./hw10 <file>\n");
        exit(1);
    }
    // attempt to open file
    int infile = open(argv[1], O_RDONLY);
    if (infile == -1){
        fprintf(stderr, "File %s not found.\n", argv[1]);
        exit(1);
    }

    // read header data
    char header[5] = {0};
    int off_size;
    int offset_arr[off_size];
    read(infile, header, 4);
    read(infile, &off_size, 4);
    for (int i = 0; i < off_size; i++) {
        read(infile, &offset_arr[i], 4);
    }

    /* debug prints
    printf("%s\n", header);
    printf("%d\n{", off_size);
    for (int i = 0; i < off_size; i++) {
        printf("%d, ", offset_arr[i]);
    }
    printf("}\n");
    end debug prints */

    // read and print each line from file,
    // according to offset array and line length
    int ln_length;
    char buffer[255];
    for (int i = 0; i < off_size; i++) {
        memset(buffer, 0, 255);
        lseek(infile, offset_arr[i], SEEK_SET);
        read(infile, &ln_length, 4);
        read(infile, buffer, ln_length - 4);
        //printf("%d: ", ln_length); //debug
        printf("%s", buffer);
    }

    exit(0);
}
