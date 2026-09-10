student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only



# Check if there's a key called 'email'. If not, ask the user to enter an email



# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string



# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method



# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.




# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores



# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 



# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".




# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".




# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100




# Recaclculate the average score and update the academic status after the course score has been updated.




# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following: 
for key, value in student.items():
    print(f"{key}: {value}")
print("-" * 30)

if 'email' not in student:
    email = input("Enter email: ")
    student['email'] = email

new_city = input("Enter new city: ")
while not new_city:
    new_city = input("City cannot be empty. Enter new city: ")
student['city'] = new_city

if student.get('phone') is None:
    phone = input("Enter phone: ")
    if phone:
        student['phone'] = phone
    else:
        print("Phone number not found.")

student['contact'] = {
    'phone': student.get('phone', 'Phone number not found.'),
    'email': student.get('email', '')
}

student['courses'] = {
    'Python': 88,
    'Databases': 91,
    'Software Engineering': 84
}

total_score = 0
course_count = 0
for score in student['courses'].values():
    total_score += score
    course_count += 1
average_score = total_score / course_count

if average_score >= 90:
    status = "Excellent"
elif average_score >= 75:
    status = "Good"
elif average_score >= 60:
    status = "Pass"
else:
    status = "At Risk"
student['academic_status'] = status

search_course = input("Enter course name to search: ")
if search_course in student['courses']:
    print(f"{search_course}: {student['courses'][search_course]}")
else:
    print("Course not found")

update_course = input("Enter course name to update: ")
if update_course in student['courses']:
    new_score = float(input("Enter new score: "))
    if 0 <= new_score <= 100:
        student['courses'][update_course] = new_score
        print(f"Score for {update_course} updated to {new_score}")
    else:
        print("Score must be between 0 and 100.")
else:
    print("Course not found")

total_score = 0
course_count = 0
for score in student['courses'].values():
    total_score += score
    course_count += 1
average_score = total_score / course_count

if average_score >= 90:
    status = "Excellent"
elif average_score >= 75:
    status = "Good"
elif average_score >= 60:
    status = "Pass"
else:
    status = "At Risk"
student['academic_status'] = status

print("STUDENT RECORD")
print("=" * 37)
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print("COURSE RESULTS")
for course, score in student['courses'].items():
    print(f"{course}: {score}")
print(f"Average Score: {average_score:.1f}")
print(f"Academic Status: {student['academic_status']}")
""" 
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """

