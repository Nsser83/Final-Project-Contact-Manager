# Final-Project-Contact-Manager
Program Description

The Contact Manager is a Python program that allows users to store and manage contact information in an organized way. The program provides a menu-driven interface where users can add new contacts, view all saved contacts, search for specific contacts, delete contacts, and update existing contact information.

Contact data is stored using a list of dictionaries, where each dictionary contains a contact’s name, phone number, and email address. The program uses a JSON file to save and load data, ensuring that contact information is preserved even after the program is closed.

The program is structured using multiple functions, each responsible for a specific task such as adding or updating contacts. It also includes input validation to ensure that names and phone numbers are not empty and that email addresses follow a basic valid format. Overall, the program is designed to be clear, functional, and user-friendly while demonstrating key programming concepts such as data handling, file operations, and control flow.
# Instructions to Run the Program
Make sure Python 3 is installed on your computer.
Copy the program code into a file and save it as contact_manager.py.
Open a terminal or command prompt.
Navigate to the folder where the file is saved.

Run the program by typing:

python contact_manager.py
A menu will appear on the screen. Enter the number corresponding to the action you want to perform (add, view, search, delete, or update contacts).
Follow the prompts to interact with the program.
The program will automatically save your contacts in a file named contacts.json in the same folder.
# Reflection

One advantage of using a program like this compared to storing data in a simple file is that it allows structured and organized data management. Instead of manually editing text, the program makes it easier to add, search, and update information efficiently.

One part of this project that was new to me was working with JSON files to save and load data. Learning how to store data permanently made the program more realistic and useful.

If I were to continue improving this project, I could add more advanced features such as better email validation, sorting contacts, or even a graphical user interface. Overall, this project helped me understand how to organize code using functions and how to build a complete, functional program that solves a real-world problem.
