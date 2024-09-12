#include <stdio.h>
#include <stdbool.h>

// Define a structure to represent a job
typedef struct {
    int deadline;
    int profit;
} Job;

// Function to swap two jobs
void swap(Job *a, Job *b) {
    Job temp = *a;
    *a = *b;
    *b = temp;
}

// Function to sort jobs by profit in descending order
void sortJobs(Job jobs[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (jobs[i].profit < jobs[j].profit) {
                swap(&jobs[i], &jobs[j]);
            }
        }
    }
}

// Function to find the maximum profit for job sequencing
int jobSequence(Job jobs[], int n) {
    // Sort jobs by profit in descending order
    sortJobs(jobs, n);
    
    // Find the maximum deadline to determine the size of the slot array
    int maxDeadline = 0;
    for (int i = 0; i < n; i++) {
        if (jobs[i].deadline > maxDeadline) {
            maxDeadline = jobs[i].deadline;
        }
    }
    
    // Initialize slot availability array
    bool slots[maxDeadline];
    for (int i = 0; i < maxDeadline; i++) {
        slots[i] = false;
    }
    
    // Initialize total profit
    int totalProfit = 0;
    
    // Job sequence
    for (int i = 0; i < n; i++) {
        // Find a slot for this job
        for (int slot = jobs[i].deadline - 1; slot >= 0; slot--) {
            if (!slots[slot]) {
                slots[slot] = true;
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    for (int i=0; i<maxDeadline; i++) {
        printf("%d ", slots[i]);
    }
    printf("\n");

    return totalProfit;
}

// Main function
int main() {
    // Example jobs (deadline, profit)
    Job jobs[] = {
        {4, 20},
        {1, 10},
        {1, 40},
        {1, 30}
    };
    int n = sizeof(jobs) / sizeof(jobs[0]);
    
    // Calculate maximum profit
    int maxProfit = jobSequence(jobs, n);
    printf("Maximum Profit: %d\n", maxProfit); // Output: Maximum Profit: 60
    
    return 0;
}
