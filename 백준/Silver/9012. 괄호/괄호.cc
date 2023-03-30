#include <iostream>
#include <stack>
using namespace std;

void fast_io(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int main(void) {
    fast_io();
    int k;
    cin >> k;
    cin.ignore();
    
    for (int i = 0; i < k; i++) {
        string str;
        getline(cin, str);
        stack<char> st;
        int ck = 0;
        
        for (int i = 0; i < str.length(); i++) {
            if (str[i] == 40 || str[i] == 91) {
                st.push(str[i]);
            }
            else if (str[i] == 41) {
                if (!st.empty() && st.top() == 40) {
                    st.pop();
                }
                else {
                    ck = 1;
                }
            }
            else if (str[i] == 93) {
                if (!st.empty() && st.top() == 91) {
                    st.pop();
                }
                else {
                    ck = 1;
                }
            }
        }

        if (st.empty() && ck == 0) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
    return 0;
}