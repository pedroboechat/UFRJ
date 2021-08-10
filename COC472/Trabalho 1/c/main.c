#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Constants declaration
int ARR_SIZE;
int JI_LOOP;
int RAND_SIZE = 100;

// A function that returns a random number between 0 and 'RAND_SIZE'
double get_random() {
    srand(time(NULL));
    return rand() % RAND_SIZE;
};

int main(int argc, char* argv[]) {

    // Checks for 'ARR_SIZE' and 'JI_LOOP' values in argv
    if (argc == 3) {
        ARR_SIZE = atoi(argv[1]);
        JI_LOOP = atoi(argv[2]);
    }
    else {
        ARR_SIZE = 5000;
        JI_LOOP = 0;
    }

    // Allocates memory for the matrixes
    double** A = (double**)malloc(sizeof(double*) * ARR_SIZE);
    double* x = (double*)malloc(sizeof(double) * ARR_SIZE);
    double* b = (double*)malloc(sizeof(double) * ARR_SIZE);
    
    // Initializes the matrixes values
    for (int i = 0; i < ARR_SIZE; i++) {
        A[i] = (double*)malloc(sizeof(double) * ARR_SIZE);
        x[i] = get_random();
        b[i] = 0;
        for (int j = 0; j < ARR_SIZE; j++) {
            A[i][j] = get_random();
        }
    }
    
    // Saves start time
    clock_t start = clock();

    // Checks for 'JI_LOOP' mode and calculates A * x = b
    if (JI_LOOP == 1) {
        for (int j = 0; j < ARR_SIZE; j++) {
            for (int i = 0; i < ARR_SIZE; i++) {
                b[i] += A[i][j] * x[j];
            }
        }
    }
    else {
        for (int i = 0; i < ARR_SIZE; i++) {
            for (int j = 0; j < ARR_SIZE; j++) {
                b[i] += A[i][j] * x[j];
            }
        }
    }

    // Prints elapsed time and prints it
    double elapsed = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("%f", elapsed);

    return 0;
}