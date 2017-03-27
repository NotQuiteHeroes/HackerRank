/*Given a square matrix of size nXn , calculate the absolute difference between the sums of its diagonals.
Input Format
The first line contains a single integer, n . The next n lines denote the matrix's rows, with each line containing n space-separated integers describing the columns.
Output Format
Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

https://www.hackerrank.com/challenges/diagonal-difference
*/

#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n, diag1 = 0, diag2 = 0;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
           
          if(a_i == a_j){
            diag1 += a[a_i][a_j];
          }
           
          if(a_i + a_j == n -1){
            diag2 += a[a_i][a_j];
          }
       }
    }
    cout<<abs(diag1-diag2);   
 
    return 0;
}
