
import json
from studymate import student_to_dict, student_from_dict

FILE_NAME = "studymate_data.json"


def save_student(student):
    print("\nSaving student details...")

    data = student_to_dict(student)

    try:
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

        print("Your details are saved.")

    except OSError:
        print("Sorry, couldn't save the details.")


def load_student():
    print("\nLooking for your saved details...")

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)

        student = student_from_dict(data)

        print("Your details are loaded.")
        return student

    except FileNotFoundError:
        print("No saved data found.")
        raise

    except json.JSONDecodeError:
        print("The saved file has some problem.")
        raise

    except OSError:
        print("Unable to open the file.")
        raise


def check_saved_file():
    try:
        with open(FILE_NAME, "r") as f:
            return True

    except FileNotFoundError:
        return False

    except OSError:
        return False


def show_saved_data():
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)

        print("\nHere is your saved data:")
        print(json.dumps(data, indent=4))

    except FileNotFoundError:
        print("You haven't saved anything yet.")

    except json.JSONDecodeError:
        print("Couldn't read the saved data.")

    except OSError:
        print("Something went wrong while opening the file.")


def clear_saved_data():
    answer = input("Do you really want to clear your saved data? (yes/no): ")

    if answer.lower() == "yes":
        try:
            with open(FILE_NAME, "w") as f:
                json.dump({}, f)

            print("Saved data cleared.")

        except OSError:
            print("Couldn't clear the data.")

    else:
        print("Okay, your data is safe.")