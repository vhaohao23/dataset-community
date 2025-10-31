#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.txt","r",stdin);
    int N=115;
    int l[N+1]={};
    int node,label;
    while (cin>>node>>label)
    {
        l[node+1]=label;
    }
    
    for (int i=1;i<=N;i++) cout<<l[i]<<",";

}