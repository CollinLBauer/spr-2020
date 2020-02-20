PGM=modules

CC=gcc
CLFAGS=-Wall

all: $(PGM)

clean:
	rm -f $(PGM)
	rm -f *.o

$(PGM):		main.o module.o
	gcc -o $@ $^