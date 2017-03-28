/* MySQL
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

https://www.hackerrank.com/challenges/weather-observation-station-11
*/

SELECT DISTINCT city FROM station WHERE city REGEXP "^[^aeiou].*" OR city REGEXP "[^aeiou]$.*";
