import pickle

class Course_grades:
    def __init__(self):
        self.Course_name = ""
        self.stu_ID = []
        self.stu_grades = []

    def get_details(self):
        self.Course_name = input("Enter the course name: ")
        for _ in range(5):
            student_id = input("Enter student ID: ")
            student_grade = float(input("Enter student grade (0-100): "))
            self.stu_ID.append(student_id)
            self.stu_grades.append(student_grade)

    def display(self):
        print(f"Course Name: {self.Course_name}")
        print("Student IDs and Grades:")
        for sid, grade in zip(self.stu_ID, self.stu_grades):
            print(f"ID: {sid}, Grade: {grade}")

def save_objects_to_file():
    f = open('grades_info.dat', 'ab')
    for _ in range(4):
        course = Course_grades()
        course.get_details()
        pickle.dump(course, f)
    f.close()
    print("Objects have been written to grades_info.dat")

def read_objects_from_file():
    try:
        f = open('grades_info.dat', 'rb')
        while True:
            try:
                course = pickle.load(f)
                course.display()
            except EOFError:
                break
        f.close()
    except FileNotFoundError:
        print("File not found! Please save objects first.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Save Course Grades to File")
        print("2. Read and Display Course Grades from File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            save_objects_to_file()
        elif choice == '2':
            read_objects_from_file()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


