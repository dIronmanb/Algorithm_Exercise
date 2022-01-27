#include <iostream>
#include <map>


using namespace std;

int main(void)
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    map<string, string>sol;

    int N, M;
    cin >> N >> M;

    string site;
    string pass;

    while(N--){
        cin >> site >> pass;
        sol.insert(make_pair(site, pass));
    }

    while(M--){
        cin >> site;
        cout << sol[site] << "\n";
    }

    return 0;
}
