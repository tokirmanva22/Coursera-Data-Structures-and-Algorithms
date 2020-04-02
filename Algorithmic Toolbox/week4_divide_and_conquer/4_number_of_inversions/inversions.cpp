#include<bits/stdc++.h>
#define ll long long int

using namespace std;

ll check(ll arr[],ll n)
{
    ll count = 0;
    for(ll i=0;i<n-1;++i)
    {
        for(ll j=i+1;j<n;++j)
        {
            if(arr[i] > arr[j])
                count++;
        }
    }
    return count;
}
main()
{
    ll n;
    cin>>n;
    ll arr[n];
    for(ll i=0;i<n;++i)
        cin>>arr[i];
    cout<<check(arr,n);
}