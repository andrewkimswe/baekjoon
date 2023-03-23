#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
	int n, k;
	cin >> n >> k;

	vector<int>coin(n);
	int cnt = 0;

	for (int i = 0; i < n; i++) {
		cin >> coin[i];
	}
	sort(coin.begin(), coin.end(), greater<int>());

	for (int i = 0; i < n; i++) {
		while (k - coin[i] >= 0) {
			cnt++;
			k -= coin[i];
		}
	}
	cout << cnt << '\n';
    return 0;
}