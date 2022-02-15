#include <stdio.h>
#define MAX 1000000    // 데이터 개수의 MAX 범위
int N, point2d[MAX][2], tmp[MAX][2]; // 데이터 개수와 저장할 배열

                     
void merge(int arr[MAX][2], int left, int right) {
     
    int L, R, k, a;
    int mid = (left + right) / 2;
    L = left;
    R = mid + 1;
    k = left;
 
    while (L <= mid && R <= right){
        
        if(arr[L][0] < arr[R][0] || arr[L][1] < arr[R][1]){
            tmp[k][0] = arr[L][0];
            tmp[k][1] = arr[L][1];
            L++;
        }

        else{
            tmp[k][0] = arr[R][0];
            tmp[k][1] = arr[R][1];
            R++;
        }
        k++;
    }

    if (L>mid) 
        for (a = R; a <= right; a++){
            tmp[k][0] = arr[a][0];
            tmp[k][1] = arr[a][1];
            k++;
        }
    else{
        for (a = L; a <= mid; a++)
            tmp[k][0] = arr[a][0];
            tmp[k][1] = arr[a][1];
            k++;
     }
    for (a = left; a <= right; a++) 
        arr[a][0] = tmp[a][0];
        arr[a][1] = tmp[a][1];  
     
}
 
 
void mergeSort(int arr[MAX][2], int left, int right) {
     
    if (left == right) return;
    int mid;
    mid = (left + right) / 2;
    mergeSort(arr, left, mid); 
    mergeSort(arr, mid + 1, right); 
    merge(arr, left, right); 
     
}

 
int main() {
    int idx;
    
    // 입력    
    scanf("%d", &N);
    for(idx = 0; idx < N; idx++) {
        scanf(" %d %d", &point2d[idx][0], &point2d[idx][1]);
    }
    
        // 출력
    for(idx = 0; idx < N; idx++) {
        printf("%d %d /" , point2d[idx][0], point2d[idx][1]);
    } printf("\n");
    
    mergeSort(point2d, 0, N - 1);    // 배열 인덱스 0 ~ N-1 까지 퀵소트
    
 
    // 출력
    for(idx = 0; idx < N; idx++) {
        printf("%d %d /" , point2d[idx][0], point2d[idx][1]);
    }printf("\n");
 
    return 0; 
}