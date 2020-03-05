#include
#include
#include












int count = 0;
pthread



















void consumer(void *arg) {

    for (int i = 0; i < loops; i++) {

        ptread_mutex_lock(&mutex);
        while (count == 0)
        pthread_cond_wait(&cond, &mutex);
    
    int tmp= get();

    pthread_cond_signam(&cond);
    pthread_mutex_unlock(&mutex);

    printf("%d\n", tmp);

    }

}
