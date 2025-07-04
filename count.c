#include <stdio.h>

int main() {
    int arr[] = {1, 2, 2, 3, 3, 3, 4};
    int freq[10] = {0};

    for (int i = 0; i < 7; i++) {
        freq[arr[i]]++;
    }

    for (int i = 0; i < 10; i++) {
        if (freq[i] != 0)
            printf("Number %d appears %d times\n", i, freq[i]);
    }

    return 0;
}
