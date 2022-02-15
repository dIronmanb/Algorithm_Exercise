// 작업 중.. 무엇이 문제인지는 미지수

#include <stdio.h>
#include <stdlib.h>

#define SWAP(x,y,temp) ((temp) = (x), (x) = (y), (y) = (temp))

void QuickSort(int nums[], int start, int end);

int main(void)
{
    int N;
    scanf("%d", &N);

    int* nums = (int*)malloc(sizeof(int) * N);
    for(int i = 0 ; i < N ; i++)
    {
        scanf("%d", &nums[i]);
    }

    QuickSort(nums, 0, N-1);


    for(int i = 0 ; i < N ; i++)
    {
        printf("%d ", nums[i]);
    }

    free(nums);
    
    return 0;
    

}



void QuickSort(int nums[], int start, int end)
{
    if(start >= end) return;


    int pivot = start + end / 2, left = start, right = end, temp;

    while(left < right){
        while(nums[left] < nums[pivot] && left < right) left++;
        while(nums[right] >= nums[pivot] && left < right) right--;

        if(left < right){
            SWAP(nums[left], nums[right], temp);
        }
    }
    SWAP(nums[pivot], nums[right], temp);

    QuickSort(nums, start, right - 1);
    QuickSort(nums , right + 1, end);
}
