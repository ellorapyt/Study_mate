
class Student:

    def __init__(self, name, daily_hours, days_left):
        self.name = name
        self.daily_hours = daily_hours
        self.days_left = days_left
        self.subjects = {}

    # Add a subject
    def add_subject(self, name, marks, confidence):

        if name in self.subjects:
            print("Subject already exists.")
            return

        self.subjects[name] = {
            "marks": marks,
            "confidence": confidence
        }

        print("Subject added successfully!")

    # Update marks
    def update_marks(self, subject, marks):

        if subject in self.subjects:
            self.subjects[subject]["marks"] = marks
            print("Marks updated.")

        else:
            print("Subject not found.")

    # Remove a subject
    def remove_subject(self, subject):

        if subject in self.subjects:
            del self.subjects[subject]
            print("Subject removed.")

        else:
            print("Subject not found.")

    # Update confidence
    def update_confidence(self, subject, confidence):

        if subject in self.subjects:
            self.subjects[subject]["confidence"] = confidence
            print("Confidence updated.")

        else:
            print("Subject not found.")

    # Show all subjects
    def show_subjects(self):

        if not self.subjects:
            print("No subjects added.")
            return

        print("\nYour Subjects:")

        for subject in self.subjects:
            print("-", subject)


# Calculate average marks
def calculate_average(student):

    if len(student.subjects) == 0:
        return 0

    total = 0

    for subject in student.subjects:
        total += student.subjects[subject]["marks"]

    return round(total / len(student.subjects), 2)


# Show performance
def show_performance(student):

    if len(student.subjects) == 0:
        print("No subjects added.")
        return

    total = 0
    highest = -1
    lowest = 101

    best_subject = ""
    weak_subject = ""

    for subject in student.subjects:

        marks = student.subjects[subject]["marks"]
        total += marks

        if marks > highest:
            highest = marks
            best_subject = subject

        if marks < lowest:
            lowest = marks
            weak_subject = subject

    average = total / len(student.subjects)

    print("\n----- Performance Report -----")
    print("Name:", student.name)
    print("Subjects:", len(student.subjects))
    print("Average marks:", round(average, 2))
    print("Highest marks:", highest)
    print("Lowest marks:", lowest)
    print("Best subject:", best_subject)
    print("Needs more practice:", weak_subject)

    if average >= 85:
        print("Excellent performance!")

    elif average >= 70:
        print("Good progress. Keep going!")

    elif average >= 50:
        print("You are making progress. Keep practising.")

    else:
        print("Try making more time for revision.")


# Suggest subjects to study
def suggest_subjects(student):

    if len(student.subjects) == 0:
        print("No subjects available.")
        return

    print("\nSubjects that need attention:")

    found = False

    for subject in student.subjects:

        marks = student.subjects[subject]["marks"]
        confidence = student.subjects[subject]["confidence"]

        if marks < 70 or confidence == "low":
            print("-", subject)
            found = True

    if not found:
        print("All subjects are looking good!")


# Make a daily study plan
def make_plan(student):

    if len(student.subjects) == 0:
        print("Add subjects first.")
        return

    total_minutes = int(student.daily_hours * 60)

    subjects = list(student.subjects.keys())

    minutes = total_minutes // len(subjects)

    print("\n----- Today's Study Plan -----")
    print("Available time:", total_minutes, "minutes")

    for subject in subjects:

        marks = student.subjects[subject]["marks"]
        confidence = student.subjects[subject]["confidence"]

        if marks < 70 or confidence == "low":
            print(subject, "-", minutes, "minutes (Revision)")

        else:
            print(subject, "-", minutes, "minutes")

    print("\nTake short breaks between study sessions.")


# Show details of each subject
def show_subject_details(student):

    if len(student.subjects) == 0:
        print("No subjects available.")
        return

    print("\n----- Subject Details -----")

    for subject in student.subjects:

        marks = student.subjects[subject]["marks"]
        confidence = student.subjects[subject]["confidence"]

        print("\nSubject:", subject)
        print("Marks:", marks)
        print("Confidence:", confidence)

        if marks >= 85:
            print("Status: Excellent")

        elif marks >= 70:
            print("Status: Good")

        else:
            print("Status: Needs improvement")


# Show subjects with low marks
def weak_subjects(student):

    print("\n----- Subjects Below 70 Marks -----")

    found = False

    for subject in student.subjects:

        marks = student.subjects[subject]["marks"]

        if marks < 70:
            print(subject, ":", marks, "marks")
            found = True

    if not found:
        print("No subjects below 70 marks.")


# Show subjects with high marks
def strong_subjects(student):

    print("\n----- Subjects Above 85 Marks -----")

    found = False

    for subject in student.subjects:

        marks = student.subjects[subject]["marks"]

        if marks >= 85:
            print(subject, ":", marks, "marks")
            found = True

    if not found:
        print("No subjects above 85 marks yet.")


# Show confidence levels
def confidence_report(student):

    if len(student.subjects) == 0:
        print("No subjects available.")
        return

    print("\n----- Confidence Report -----")

    for subject in student.subjects:

        confidence = student.subjects[subject]["confidence"]

        print(subject, ":", confidence)

        if confidence == "low":
            print("Try revising this subject more often.")

        elif confidence == "medium":
            print("Regular practice may help.")

        elif confidence == "high":
            print("Keep revising to maintain confidence.")


# Show student information
def show_student_info(student):

    print("\n----- Student Profile -----")

    print("Name:", student.name)
    print("Daily study hours:", student.daily_hours)
    print("Days left for exam:", student.days_left)
    print("Total subjects:", len(student.subjects))
    print("Average marks:", calculate_average(student))


# Convert student object into dictionary
def student_to_dict(student):

    data = {
        "name": student.name,
        "daily_hours": student.daily_hours,
        "days_left": student.days_left,
        "subjects": student.subjects
    }

    return data


# Convert dictionary into student object
def student_from_dict(data):

    student = Student(
        data["name"],
        data["daily_hours"],
        data["days_left"]
    )

    student.subjects = data["subjects"]

    return student