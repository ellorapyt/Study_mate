
from studymate import Student, show_performance, make_plan, suggest_subjects
from storage import save_student, load_student


def get_number(message, kind=float):
    while True:
        try:
            return kind(input(message))
        except ValueError:
            print("Please enter a number.")


def start():
    print("\nWelcome to StudyMate!")
    print("Let's make your study profile.\n")

    name = input("Enter your name: ")
    hours = get_number("How many hours can you study daily? ")
    days = get_number("How many days are left for your exam? ", int)

    student = Student(name, hours, days)

    total = get_number("How many subjects do you have? ", int)

    for i in range(total):
        print("\nSubject", i + 1)

        subject = input("Enter subject name: ")
        marks = get_number("Enter your marks: ")
        confidence = input("Confidence (low/medium/high): ").lower()

        try:
            student.add_subject(subject, marks, confidence)
            print("Subject added!")

        except ValueError as e:
            print("Could not add subject:", e)

    while True:
        print("\n------ StudyMate Menu ------")
        print("1. Check performance")
        print("2. Get study suggestions")
        print("3. Make a study plan")
        print("4. Update marks")
        print("5. Save profile")
        print("6. Load profile")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        try:
            if choice == "1":
                show_performance(student)

            elif choice == "2":
                suggest_subjects(student)

            elif choice == "3":
                make_plan(student)

            elif choice == "4":
                subject = input("Which subject? ")
                marks = get_number("Enter your new marks: ")

                student.update_marks(subject, marks)
                print("Marks updated!")

            elif choice == "5":
                save_student(student)
                print("Your profile is saved.")

            elif choice == "6":
                student = load_student()
                print("Your profile is loaded.")

            elif choice == "0":
                print("Thanks for using StudyMate!")
                print("Good luck with your exams!")
                break

            else:
                print("Please select a valid option.")

        except (ValueError, KeyError, FileNotFoundError) as e:
            print("Something went wrong:", e)


if __name__ == "__main__":
    start()