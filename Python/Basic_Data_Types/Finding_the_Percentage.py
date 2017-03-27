'''
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer n followed by the names and marks for n students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
Input Format
The first line contains the integer n, the number of students. The next n lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
Constraints
2 <= n <=100
0 <= Marks <= 100
Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

https://www.hackerrank.com/challenges/finding-the-percentage
'''

n = input()
i = 0
gradebook = {}

while i < n:
    student_info = raw_input().split()
    name = student_info[0]
    math = float(student_info[1])
    phys = float(student_info[2])
    chem = float(student_info[3])
    
    gradebook[name] = {"Math": math, "Physics": phys, "Chemistry":chem}
    
    i+=1
    
searchName = raw_input()

average = (gradebook[searchName]['Math'] + gradebook[searchName]["Physics"] + gradebook[searchName]["Chemistry"])/3

print("%.2f" % average)
