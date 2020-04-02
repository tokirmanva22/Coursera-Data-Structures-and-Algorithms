#include<bits/stdc++.h>
#define ll long long int

using namespace std;
int check(ll arr[],ll n)
{
    map<ll,ll> amap;
    for(ll i=0;i<n;++i)
    {
        ++amap[arr[i]];
        if (amap[arr[i]] > n/2)
        {
            return 1;
        }
    }
    return 0;
}

main()
{
    ll n;
    cin>>n;
    ll arr[n];
    for(ll i=0;i<n;++i)
    {
        cin>>arr[i];
    }
    cout<<check(arr,n);
}