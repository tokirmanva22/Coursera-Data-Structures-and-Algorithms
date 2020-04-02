#include <bits/stdc++.h>
using namespace std;
#define ll long long int
ll MaxPairwiseProduct(const vector<ll>& numbers) {
    ll max_product = 0, a = -1, b = -1;
    ll n = numbers.size();
    // if( numbers[0] > numbers[1])
    // 	{
    // 		a = numbers[0];
    // 		b = numbers[1] ;
    // 	}
    // else{
    // 		b = numbers[0];
    // 		a = numbers[1] ;
    // } 
    for(ll i=0; i<n; ++i )
    {
    	if(numbers[i] > a)
    	{
    		if(a > b)
    			b = a;
    		a = numbers[i];
    	}
    	else if(numbers[i] > b)
    		b = numbers[i];
    }
    max_product = a*b ;

    return max_product;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> numbers(n);
    for (ll i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
