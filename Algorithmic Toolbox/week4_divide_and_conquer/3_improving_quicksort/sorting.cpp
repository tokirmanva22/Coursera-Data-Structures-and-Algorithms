#include<bits/stdc++.h>
#define ll long long int

using namespace std;

void print(ll arr[], ll n)
{
    for(ll i=0;i<n;++i)
        cout<<arr[i]<<" ";
}

int partition(ll arr[],ll low,ll high)
{
    ll pivot = arr[high];
    ll i = low-1;
    for(ll j = low;j<high;++j)
    {
        if(arr[j]<= pivot)
        {
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[high]);
    return i+1 ;
    
    
}

int part_rand(ll arr[],ll low,ll high)
{
    ll random = low + rand() % (high-low) ;
    swap(arr[random],arr[low]);
    return partition(arr,low,high);
}
void quickSort(ll arr[],ll low,ll high)
{
    if(low<high)
    {
        ll pi = part_rand(arr,low,high);
        
        quickSort(arr,low,pi-1);
        quickSort(arr,pi+1,high);
    }
}
main()
{
    ll n;
    cin>>n;
    ll arr[n];
    for(ll i=0;i<n;++i)
        cin>>arr[i];
    quickSort(arr,0,n-1);
    print(arr,n);
}