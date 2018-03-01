/*
At HackerLand University, a passing grade is any grade 40 points or higher on a 100 point scale. Sam is a professor at the university and likes to round each student’s grade according to the following rules:

If the difference between the grade and the next higher multiple of 5 is less than 3, round to the next higher multiple of 5
If the grade is less than 38, don’t bother as it’s still a failing grade
Automate the rounding process then round a list of grades and print the results.

Sample input:
4
73
67
38
33

Sample output:
75
67
40
33

*/

#include <vector>
#include <iostream>


using namespace std;


int main(){
    int n;
    cin >> n;
    for(int a0 = 0; a0 < n; a0++){
        int grade;
        cin >> grade;
        if(grade < 38 || grade % 5 == 0){
            cout<<grade<<endl;
        }
        else if(((grade+2)%5 == 0)||((grade+1)%5==0)){
            while(grade % 5 != 0){
                grade++;
            }
            cout<<grade<<endl;
        }
        else{
            cout<<grade<<endl;
        }
    }
    return 0;
}
