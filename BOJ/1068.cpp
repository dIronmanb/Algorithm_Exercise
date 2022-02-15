/*
    조건
    - 해당 트리에서 각 리프 노드의 개수를 추출
    - 삭제된 ㅇ 

*/

#include <bits/stdc++.h>
using namespace std;

int N, Cut;
vector<int> adj[55];

int DFS(int curr){
	int ret = 1;
	int child = 0;
	for (auto ch: adj[curr]){
		if(ch==Cut) continue;
		child += DFS(ch);
	}
	// 리프노드가 아닌경우 
	if(child) return child;
	// 리프노드인경우 ( 자식이 없는경우) 
	else return ret;
}

int main(){ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);

cin >> N;
int Root;
for (int i = 0; i < N; ++i){
	int parent;
	cin >> parent;
	if(parent==-1) Root=i;
	else adj[parent].push_back(i);
}
cin >> Cut;

if(Root!=Cut) cout << DFS(Root) << '\n';
else cout << 0 << '\n';

return 0;
} 	