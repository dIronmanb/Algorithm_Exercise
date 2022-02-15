// 수 정렬하기3
#include <iostream>

using namespace std;

int nums[10001] = {0};


int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, idx;
    cin >> N;

    for(int i = 0 ; i < N ; i++){
        cin >> idx;
        nums[idx] += 1;
    }
    
    for(int i = 0 ; i < 10001 ; i++){

        if(nums[i] != 0)
            for(int j = 1; j <= nums[i] ; j++)
                cout << i << '\n';
    }

    return 0;
}