all: guarded unguarded thread

clean:
	rm -r guarded.out unguarded.out thread.out

guarded: guarded.c
	gcc -Wall -o guarded.out guarded.c

unguarded: unguarded.c
	gcc -Wall -o unguarded.out unguarded.c

thread: ThreadData.c
	gcc -Wall -o thread.out ThreadData.c