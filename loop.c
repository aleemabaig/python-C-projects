#include <stdio.h>

int main() {
    int arr[5] = {14, 22, 5, 63, 30};
    int max = arr[0];

    for (int i = 1; i < 5; i++) {
        if (arr[i] > max)
            max = arr[i];
    }

    printf("Maximum value: %d\n", max);
    return 0;
}
