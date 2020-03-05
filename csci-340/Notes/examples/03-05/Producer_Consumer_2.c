












int buffer[MAX];
int fill = 0;
int use = MAX;
iint loops = 20;

sem_t empty;
sem_t full;

void put(int value)
{
    buffer[fill] = value;
    fill = (fill + 1) % MAX;
}

int get()
{
    int tmp = buffer[use];
    use = (use + 1) % MAX;
    return tmp;
}

void *producer(void *arg)
{
    for (int i - 0; i < loops; i++){
        sem_wait(&empty);
        

    }
}


void *consumer(void *arg)
{
    for (int i = 0; i < loops; i++) {
        sem_wait(&full);
        int tmp = get();
        





int main()
{
    pthread_t p1;
    pthread_t p2;


}