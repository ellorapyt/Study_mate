# 📚 StudyMate — Your Personal Study Assistant

StudyMate is a simple Python-based study assistant designed to help students organize their subjects, track academic performance, and plan their study time.

It uses a command-line interface, making it easy to use and understand. Student data can be saved in a JSON file and loaded again whenever needed.

## ✨ Features

- Add subjects and set target marks.
- Update marks and track subject performance.
- View an overview of academic progress.
- Get study recommendations based on marks.
- Create a study plan for subjects that need more attention.
- Save and load student data using JSON.
- Run unit tests to check important functions.

## 🛠️ Technologies Used

- **Python 3** — Main programming language
- **JSON** — Data storage
- **unittest** — Testing the application

## 📁 Project Structure

```text
StudyMate/
│
├── main.py             # Main menu and user interaction
├── studymate.py        # Student class and study-related functions
├── storage.py          # Saving and loading student data
├── test_studymate.py   # Unit tests
└── README.md           # Project documentation
📖 How to Use

When the program starts, use the menu to access the available features:

Add a subject.

Update marks.

View academic performance.

Get study recommendations.

Create a study plan.

Save student data.

Load saved data.

Exit the application.

The available options will be displayed in the terminal.

💾 Data Storage

StudyMate uses a JSON file to store student and subject information.

This allows your data to be saved between sessions and loaded again when you use the application.

🧪 Running the Tests

The project includes unit tests for checking its core functionality.

Run the tests using:

python -m unittest
🧠 Python Concepts Practiced

This project demonstrates the use of:

Classes and objects

Functions and modules

Lists and dictionaries

Loops and conditional statements

File handling

JSON serialization

Exception handling

Unit testing

🔮 Future Improvements

Possible improvements for future versions include:

A graphical user interface

Study reminders

Weekly progress reports

Performance charts

A calendar-based study planner

📝 Project Note

StudyMate is an educational project created to help students organize their studies. Its recommendations are based on simple rules and the marks entered by the user. They are intended as study guidance rather than predictions of academic results.