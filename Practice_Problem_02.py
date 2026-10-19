'''Problem 2 — Student Marks Calculator
Write a Python program that accepts a student's name and marks in three subjects. Calculate and display the total marks, 
average marks, and percentage. Assume each subject carries a maximum of 100 marks.'''

student_name = (input("Type student name: "))
mark = {
    "Physics"       : int(input("type physics marks: ")),
    "Chemistry"     : int(input("type Chemistry marks: ")),
    "Math's"        : int(input("type Maths marks: "))
}

#calculations
total_marks = sum(mark.values())
avg_marks = total_marks/len(mark)
percentage = (total_marks/(len(mark)*100))*100

#Report
print("\n========== Report Card ==========")
print(f"{'Student Name':<15}:{student_name}")
print(f"{'Total Marks':<15}:{total_marks:.2f}")
print(f"{'Avg Marks':<15}:{avg_marks:.2f}")
print(f"{'Percentage':<15}:{percentage:.2f}%")
print("\n========== Report End ===========")

