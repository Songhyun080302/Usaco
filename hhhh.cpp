#include <iostream>
#include <vector>
#include <set>
#include <unordered_set> // Include this header
#include <algorithm> 

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    unordered_set<string> moos; // Now this line should compile

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (arr[i] != arr[j]) {
                vector<int> temp_arr = arr; 
                temp_arr.erase(remove(temp_arr.begin(), temp_arr.end(), arr[i]), temp_arr.end());
                temp_arr.erase(remove(temp_arr.begin(), temp_arr.end(), arr[j]), temp_arr.end());

                if (count(temp_arr.begin(), temp_arr.end(), arr[j]) != 2) {
                    continue; 
                }

                string moo = to_string(arr[i]) + " " + to_string(arr[j]) + " " + to_string(arr[j]);
                moos.insert(moo);
            }
        }
    }

    cout << moos.size() << endl;
    return 0;
}
