/* MS SQL
Let N be the number of CITY entries in STATION, and let N1 be the number of distinct CITY names in STATION; query the value of N - N1 from STATION. In other words, find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
*/

SELECT(SELECT COUNT(CITY) FROM STATION) - (SELECT COUNT(DISTINCT CITY) FROM STATION);
