/*Consider a staircase of size n = 4:
   #
  ##
 ###
####
Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.
Input Format
A single integer, n, denoting the size of the staircase.
Output Format
Print a staircase of size n using # symbols and spaces.
Note: The last line must have 0 spaces in it.

https://www.hackerrank.com/challenges/staircase
*/

#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n, k, j, p = 1;
    cin >> n;
    k = n-1;
        
    for(int i = 0; i < n; i++){
        j = k;
        for(int l = 0; l < j; l++){
            cout<<" ";
        }
        for(int m = 0; m < p; m++){
            cout<<"#";
        }
        cout<<endl;
        
        k--;
        p++;

    }
    return 0;
}
