#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    printf("Original array: ");
    for (int i = 0; i < 5; i++)
        printf("%d ", arr[i]);

    printf("\nReversed array: ");
    for (int i = 4; i >= 0; i--)
        printf("%d ", arr[i]);

    return 0;
}
