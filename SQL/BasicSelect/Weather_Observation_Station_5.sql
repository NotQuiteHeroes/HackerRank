/* MySQL
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

https://www.hackerrank.com/challenges/weather-observation-station-5
*/

SELECT city, LENGTH(city) AS maxlen
FROM station
ORDER BY
    maxlen DESC
LIMIT 1;

SELECT city, LENGTH(city) AS minLen
FROM station
ORDER BY
    minlen ASC
LIMIT 1;
