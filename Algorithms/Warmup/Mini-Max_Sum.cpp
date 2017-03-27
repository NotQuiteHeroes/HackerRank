/*Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Input Format
A single line of five space-separated integers.
Output Format
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

https://www.hackerrank.com/challenges/mini-max-sum
*/

#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    long int a;
    long int b;
    long int c;
    long int d;
    long int e;
    cin >> a >> b >> c >> d >> e;
    
    vector<long int> nums;
    nums.push_back(a);
    nums.push_back(b);
    nums.push_back(c);
    nums.push_back(d);
    nums.push_back(e);
    
    sort(nums.begin(), nums.end());
    
    long int max = 0, min = 0, sum = 0;
    for(int i = 0; i < 5; i++){
        sum+=nums.at(i);
    }
  
    max = sum-nums.at(0);
    min = sum-nums.at(4);
    
    cout<<min<<" "<<max;
    return 0;
}
