/*Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Input Format
A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ), where 01 <= hh <= 12 and 00 <= mm, ss <= 59.
Output Format
Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

https://www.hackerrank.com/challenges/time-conversion
*/


#include <string>
#include <iostream>

using namespace std;

int main(){
    string time, x;
    int temp;
    cin >> time;
        
    if(time.substr(8, 2) == "PM"){
        if(time.substr(0, 2) == "12"){
            cout<<time.substr(0, 8);
        }
        else{
            temp = stoi(time.substr(0,2));
            temp = 12 + temp;
            cout<<temp<<time.substr(2, 6);
        }
    }
    else{
        if(time.substr(0,2) == "12"){
            x = "00";
            cout<<x<<time.substr(2, 6);
        }
        else{
           cout<<time.substr(0, 8); 
        }     
 
    }
    
    return 0;
}
