import csv
import random

# Define the dataset parameters
filename = "student_dataset.csv"
departments = ["Computer Science", "Cybersecurity", "Information Technology", "Software Engineering"]
levels = [100, 200, 300, 400]
num_students = 50

# Create and write to the CSV file
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the column headers
    writer.writerow([
        "Student ID", 
        "Department", 
        "Level", 
        "Attendance Percentage", 
        "Average Examination Score"
    ])
    
    # Generate fictional data for each student
    for i in range(1, num_students + 1):
        student_id = f"STU{2026000 + i}"
        department = random.choice(departments)
        level = random.choice(levels)
        attendance = round(random.uniform(45.0, 100.0), 1) # Random float between 45 and 100
        score = round(random.uniform(35.0, 98.0), 1)       # Random float between 35 and 98
        
        writer.writerow([student_id, department, level, attendance, score])

print(f"Success! The fictional dataset has been saved to {filename}")