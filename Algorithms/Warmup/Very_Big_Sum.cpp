/*You are given an array of integers of size N. You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.
Input Format
The first line of the input consists of an integer n. The next line contains n space-separated integers contained in the array.
Output Format
Print a single value equal to the sum of the elements in the array.

https://www.hackerrank.com/challenges/a-very-big-sum
*/

#include <vector>
#include <iostream>

using namespace std;


int main(){
    int n;
    long sum = 0;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
       sum += arr[arr_i];
    }
    cout<<sum;
    return 0;
}
