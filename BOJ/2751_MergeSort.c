#include <stdio.h>
#define MAX 1000000    // 데이터 개수의 MAX 범위
int N, data[MAX], tmp[MAX]; // 데이터 개수와 저장할 배열

                     
void merge(int arr[], int left, int right) {
     
    int L, R, k, a;
    int mid = (left + right) / 2;
    L = left;
    R = mid + 1;
    k = left;
 
    while (L <= mid && R <= right)
        tmp[k++] = arr[L] <= arr[R] ? arr[L++] : arr[R++];
 
    if (L>mid) 
        for (a = R; a <= right; a++)
            tmp[k++] = arr[a];
    else
        for (a = L; a <= mid; a++)
            tmp[k++] = arr[a];
     
    for (a = left; a <= right; a++) 
        arr[a] = tmp[a];
     
}
 
 
void mergeSort(int arr[], int left, int right) {
     
    if (left == right) return;
    int mid;
    mid = (left + right) / 2;
    mergeSort(arr, left, mid); 
    mergeSort(arr, mid + 1, right); 
    merge(arr, left, right); 
     
}
/*
#include<stdio.h>
#define MAX 1000000    // 데이터 개수의 MAX 범위
int N, arr[MAX], buf[MAX]; // 데이터 개수와 저장할 배열


void MergeSort(int data[], int start, int end);
void Merge(int data[], int start, int mid, int end);
*/
 
int main() {
    int idx;
    
    // 입력    
    scanf("%d", &N);
    for(idx = 0; idx < N; idx++) {
        scanf("%d", &data[idx]);
    }
    
    mergeSort(data, 0, N - 1);    // 배열 인덱스 0 ~ N-1 까지 퀵소트
    
 
    // 출력
    for(idx = 0; idx < N; idx++) {
        printf("%d " , data[idx]);
    }
 
    return 0; 
}


/*
void MergeSort(int data[], int start, int end)
{
    // 데이터 split
    if(start < end){
        int mid = (start + end) / 2;
        MergeSort(data, start, mid);
        MergeSort(data, mid + 1, end);
        Merge(data, start, mid, end);
    }
    
}

void Merge(int data[], int start, int mid, int end)
{
    // 순서대로 삽입
    int i = start, j = mid + 1, k = start; // start == mid인 경우를 방지하기 위해서!
    
    while(i <= mid && j < end){
        if(data[i] <= data[j]){
            buf[k++] = data[i++];
        }
        else{
            buf[k++] = data[j++];
        }
    }

    // 나머지 데이터 삽입
    if(i > mid){
        for(int t = j ; t < end ; t++){
            buf[k++] = data[t];
        }
    }
    else{
        for(int t = i ; t <= mid ; t++){
            buf[k++] = data[t];
        }
    }

    for(int t = start ; t <= end ; t++){
        data[t] = buf[t];
    }
}

*/