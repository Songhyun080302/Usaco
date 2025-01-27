#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    // Create a set to store distinct moos
    unordered_set<string> moos;

    // Iterate through the array
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (arr[i] != arr[j]) {
                // Check if a moo can be formed with arr[i], arr[j], and arr[j]
                bool possible = true;
                vector<int> temp_arr = arr;
                temp_arr.erase(remove(temp_arr.begin(), temp_arr.end(), arr[i]), temp_arr.end());
                temp_arr.erase(remove(temp_arr.begin(), temp_arr.end(), arr[j]), temp_arr.end());
                if (count(temp_arr.begin(), temp_arr.end(), arr[j]) != 2) {
                    possible = false;
                }
                if (possible) {
                    // Construct the moo string
                    string moo = to_string(arr[i]) + " " + to_string(arr[j]) + " " + to_string(arr[j]);
                    moos.insert(moo);
                }
            }
        }
    }

    cout << moos.size() << endl;
    return 0;
}
