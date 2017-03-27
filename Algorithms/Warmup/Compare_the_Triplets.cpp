/*Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1  to 100  for three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2), and the rating for Bob's challenge to be the triplet B = (b0, b1, b2).
Your task is to find their comparison points by comparing a0 with b0 , a1 with b1 , and a2  with b2 .
If ai > bi , then Alice is awarded  point.
If ai < bi, then Bob is awarded  point.
If ai = bi, then neither person receives a point.
Comparison points is the total points a person earned.
Given A and B , can you compare the two challenges and print their respective comparison points?
Input Format
The first line contains  space-separated integers, , , and , describing the respective values in triplet . 
The second line contains  space-separated integers, , , and , describing the respective values in triplet .
Output Format
Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

https://www.hackerrank.com/challenges/compare-the-triplets
*/

#include <iostream>

using namespace std;

int main(){
    int a0;
    int a1;
    int a2;
    cin >> a0 >> a1 >> a2;
    int b0;
    int b1;
    int b2;
    cin >> b0 >> b1 >> b2;
    
    int alice = 0, bob = 0;
    alice = (((a0>b0)? 1:0)+((a1>b1)? 1:0)+((a2>b2)? 1:0));
    bob = (((b0>a0)? 1:0)+((b1>a1)? 1:0)+((b2>a2)? 1:0));
    
    cout<<alice<<" "<<bob;
    
    return 0;
}
