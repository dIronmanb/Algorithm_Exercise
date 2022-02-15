/*
    11725번ㅣ 트리의 부모 노드 찾기
    먼저 입력한 값들을 tree에 넣는다. (이때 트리는 이진트리)
    각 트리를 DFS(깊이 우선 탑색으로 진행한다.)

    
*/

#include <iostream>
#include <vector>

using namespace std;

 

const int MAX = 100000 + 1; // 최대 배열 크기
 

int N;
bool visited[MAX];
int parent[MAX];

vector<int> tree[MAX]; // 1차원 배열의 벡터

 

void findParent(int nodeNum)
{
        visited[nodeNum] = true; //방문한 노드 표시

        //DFS
        for (int i = 0; i<tree[nodeNum].size(); i++) //해당 트리 노드에서 연결된 트리 개수만큼 루프
        {
                 int next = tree[nodeNum][i]; // next는 해당 트리 노드에 연결된 다음 노드값
                 if (!visited[next]) //next가 아직 방문되지 않았다면
                 {
                         parent[next] = nodeNum; //next의 parent는 nodeNum
                         findParent(next);
                 }

        }

}


int main(void)
{

        ios_base::sync_with_stdio(0);
        cin.tie(0); //cin 속도 향상 위해


        cin >> N; 

        for (int i = 0; i < N - 1; i++)
        {

                 int node1, node2;
                 cin >> node1 >> node2;

                 tree[node1].push_back(node2);
                 tree[node2].push_back(node1);
        }

        findParent(1); //root부터

 

        //endl 사용 시 시간 초과
        for (int i = 2; i <= N; i++)
                 cout << parent[i] << "\n";

        return 0;

}

