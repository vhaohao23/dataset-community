#include<bits/stdc++.h>
using namespace std;
map<string,int> mp;
int main(){
    freopen("input.txt","r",stdin);
    freopen("dolphins.txt","w",stdout);
    string s;
    int N=0;
    int i=0;
    vector<string> edgelist;
    string s1;
    string s2;

    while(cin>>s){
        if(mp.find(s)==mp.end()){
            mp[s]=++N;
        }

        i++;
        if (i%2==1) s1=s;
        else s2=s;

        if (i%2==0) {
            edgelist.push_back(to_string(mp[s1])+" "+to_string( mp[s2]) );
            s="";
        }
    }

    cout<<N<<" "<<i/2<<"\n";
    for (string edge:edgelist) cout<<edge<<"\n";
}