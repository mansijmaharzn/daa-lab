#include<stdio.h>

void getArray(int arr[], int size) {
    printf("Enter values for array:\n");
    for (int i=0; i<size; i++) {
        printf("arr[%d]: ", i);
        scanf("%d", &arr[i]);
    }
}

void displayArray(int arr[], int size) {
    printf("Array: ");
    for (int i=0; i<size; i++) {
        printf("%d\t", arr[i]);
    }
    printf("\n");
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[low];  // Use the first element as the pivot
    int i = low + 1;  // Start from the element after the pivot
    int j = high;

    while (i <= j) {
        // Move 'i' to the right until we find an element greater than pivot
        while (i <= high && arr[i] <= pivot) {
            i++;
        }

        // Move 'j' to the left until we find an element smaller than pivot
        while (j >= low && arr[j] > pivot) {
            j--;
        }

        // Swap the elements if they are in the wrong order
        if (i < j) {
            swap(&arr[i], &arr[j]);
        }
    }

    // Place the pivot in the correct position
    swap(&arr[low], &arr[j]);

    return j;  // Return the position of the pivot
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);  // Sort elements before partition
        quickSort(arr, pi + 1, high); // Sort elements after partition
    }
}

int main() {
    int arr[5];

    getArray(arr, 5);

    quickSort(arr, 0, 4);

    displayArray(arr, 5);
    
    return 0;
}
