#include <bits/stdc++.h>
using namespace std;

int main(){
    cout << "\n";
    string sub, full;
    int cnt=0, k=0, j=0, i;
    cin >> full >> sub;
    while (k < full.length()) {
        if (k == full.length()-1)
            cout << "Substring doesn't exist";
        if (cnt == sub.length()) {
            //cout<< "cnt is : " << cnt <<"\n";
            cout << "Substring exists\n";
            break;
        }
        else if (sub[j++] == full[i++]) {
            //cout << "comparisons (j,i): (" <<j-1<<","<<i-1<<")\n";
            cnt++;
            
        }
        else {
            k++;
            j = 0;
            i = k;
            cnt = 0;
        }
    }

}
