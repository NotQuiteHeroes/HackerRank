/* MySQL
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

https://www.hackerrank.com/challenges/weather-observation-station-6
*/

SELECT DISTINCT city FROM station WHERE city REGEXP "^[aeiou].*";
