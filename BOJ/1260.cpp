#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
int start;
vector<int> array[1000];
int visited1[1000] = {0};
int visited2[1000] = {0};

void dfs(int x){
    if(visited1[x]) return;
    visited1[x] = true;

    cout << x <<  ' ';
    for(int i = 0 ; i < array[x].size() ; i++){
        int val = array[x][i];
        dfs(val);
    }
}

void bfs(int x){
    queue<int> q;
    q.push(x);
    visited2[x] = true;
    
    while(!q.empty()){
        int a = q.front();
        q.pop();
        cout << a << ' ';
        for(int i = 0 ; i < array[x].size() ; i++){
            int y = array[x][i];
            if(!visited2[i]){
                visited2[i] = true;
                q.push(y);
            }
        }
    }
}


int main(void)
{
    cin >> N >> M >> start;
    int a,b;

    for(int i = 0 ; i < M ; i++){
        cin >> a >> b;
        array[a].push_back(b);
        array[b].push_back(a);
    }

    dfs(start); cout << '\n';
    bfs(start); cout << '\n';

    return 0;
}
