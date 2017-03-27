/*Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places.
Input Format
The first line contains an integer, n, denoting the size of the array. 
The second line contains n space-separated integers describing an array of numbers.
Output Format
You must print the following 3 lines:
A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.

https://www.hackerrank.com/challenges/plus-minus
*/

#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n;
    float p, ne, z;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
       
        if(arr[arr_i] < 0){
            ne = ne + 1;
        }
        if(arr[arr_i] > 0){
            p = p + 1;
        }
        if(arr[arr_i] == 0) {
            z = z + 1;
        }
        
    }
    cout<<p/n<<endl;
    cout<<ne/n<<endl;
    cout<<z/n<<endl;
    return 0;
}
