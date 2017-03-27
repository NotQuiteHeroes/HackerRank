/*Given an array of  integers, can you find the sum of its elements?
Input Format
The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.
Output Format
Print the sum of the array's elements as a single integer.

https://www.hackerrank.com/challenges/simple-array-sum
*/

#include <vector>
#include <iostream>


using namespace std;


int main(){
    int n, sum = 0;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
       sum += arr[arr_i];
    }
    cout<<sum;
    
    return 0;
}
