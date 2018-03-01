/*
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Sam’s two children, Larry and Rob, decide to play a game in which they each climb a tree and throw fruit at their (Sam’s) house. Each fruit that lands on the house scores one point for the one who threw it. Larry climbs the tree on the left (the apple), and Rob climbs the one on the right (the orange).

For simplicity, we’ll assume all of the landmarks are on a number line. Larry climbs the apple tree at point a, and Rob climbs the orange tree at point b. Sam’s house stands between points s and t. Values increase from left to right.

You will be given a list of distances the fruits are thrown. Negative distances indicate travel left and positive distances, travel right. Your task will be to calculate the scores for Larry and Rob and report them each on a separate line.

Input format:
2 space-separated integers s and t, left and right sides of Sam’s house
2 space-separated integers a and b, Larry’s and Rob’s positions in the trees
2 space-separated integers m and n, number of apples and oranges thrown
m space-separated integers - distances mi that each apple falls from a
n space-separated integers - distances ni that each orange falls from b

Sample Input:
7 11
5 15
3 2
-2 2 1
5 -6

Sample output:
1 1

*/

#include <vector>
#include <iostream>


using namespace std;


int main(){
    int s;
    int t;
    cin >> s >> t;
    int a;
    int b;
    cin >> a >> b;
    int m;
    int n;
    int appleCount, orangeCount;
    cin >> m >> n;
    vector<int> apple(m);
    for(int apple_i = 0;apple_i < m;apple_i++){
       cin >> apple[apple_i];
       if((apple[apple_i]+a) >= s && (apple[apple_i]+a) <= t){
           appleCount++;
       }
    }
    vector<int> orange(n);
    for(int orange_i = 0;orange_i < n;orange_i++){
       cin >> orange[orange_i];
       if((orange[orange_i]+b) >= s && (orange[orange_i]+b) <= t){
           orangeCount++;
        }
    }
    
    cout<<appleCount<<"\n"<<orangeCount;
        
    return 0;
}
