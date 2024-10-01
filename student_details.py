'''
Python program to get the student details
Author:Divya Kuriakose
Date:01-10-2024
version:1.0
'''

name=input("Enter the student name:")
roll_number=int(input("Enter your roll_nuber:"))
roll_number=roll_number+1
cgpa=float(input("Enter the CGPA:"))
percentage_mark= cgpa*10
print("Name of the student:",name)
print("Roll_number:",roll_number)
print("Mark Percentage",percentage_mark,"%")