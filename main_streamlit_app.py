import json
import os
import streamlit as st

# Function to initialize the database
def init_database():
    if not os.path.exists("database/data.json"):
        os.makedirs("database", exist_ok=True)
        with open("database/data.json", "w") as file:
            data = {
                "admin": {
                    "admin": "josh",
                    "password": "secret"
                },
                "users": {
                    "1": {
                        "username": "josh",
                        "email": "josh@example.com",
                        "rollNumber": "1"
                    }
                }
            }
            json.dump(data, file, indent=4)

# Function to load the database
def load_database():
    with open("database/data.json", "r") as file:
        return json.load(file)

# Function to save the database
def save_database(data):
    with open("database/data.json", "w") as file:
        json.dump(data, file, indent=4)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'admin' not in st.session_state:
    st.session_state.admin = ""

if 'password' not in st.session_state:
    st.session_state.password = ""

init_database()

# Main app
def main():
    if not st.session_state.logged_in:
        st.title("Student Management System")
        st.session_state.adminUsername = st.text_input("Enter your admin username:")
        st.session_state.adminPassword = st.text_input("Enter your admin password:", type="password")
        
        if st.button("Login"):
            data = load_database()
            admin = data["admin"]["admin"]
            password = data["admin"]["password"]

            if st.session_state.adminUsername == admin and st.session_state.adminPassword == password:
                st.session_state.logged_in = True
                st.session_state.admin = admin
                st.session_state.password = password
                st.success(f"Welcome back, {admin}")
            else:
                st.error("Incorrect username or password!")
    else:
        main_menu()

def main_menu():
    st.header("Main Menu")
    choice = st.selectbox("What would you like to do?", 
                          ['Add a new student', 'Edit an existing student', 'Delete an existing student', 'View all students'])

    if choice == 'Add a new student':
        add_student()
    elif choice == 'Edit an existing student':
        edit_student()
    elif choice == 'Delete an existing student':
        del_student()
    elif choice == 'View all students':
        view_all_students()

def add_student():
    student_username = st.text_input("Enter the username of the student:")
    student_email = st.text_input("Enter the email of the student:")

    if st.button("Add Student"):
        data = load_database()
        users = data["users"][0]
        student_key = str(len(users) + 1)

        student_data = {
            student_key: {
                "username": student_username,
                "email": student_email,
                "rollNumber": student_key
            }
        }

        users.update(student_data)
        save_database(data)
        st.success("Student added successfully!")

def edit_student():
    student_key = st.text_input("Enter the Key of the student you want to edit:")
    
    if st.button("Load Student Data"):
        data = load_database()
        student_data = data["users"][0]
        
        if student_key in student_data:
            st.session_state.student_key = student_key
            st.session_state.student_username = student_data[student_key]["username"]
            st.session_state.student_email = student_data[student_key]["email"]
            st.session_state.student_loaded = True
        else:
            st.error("Please, enter a correct Key!")

    if 'student_loaded' in st.session_state and st.session_state.student_loaded:
        new_username = st.text_input("Enter the new username:", value=st.session_state.student_username)
        new_email = st.text_input("Enter the new email:", value=st.session_state.student_email)
        
        if st.button("Update Student"):
            data = load_database()
            student_data = data["users"][0]
            student_key = st.session_state.student_key
            
            student_data[student_key]["username"] = new_username
            student_data[student_key]["email"] = new_email
            save_database(data)
            st.success("Student updated successfully!")
            st.session_state.student_loaded = False

def del_student():
    student_key = st.text_input("Enter the Key of the student you want to delete:")
    if st.button("Delete Student"):
        data = load_database()
        student_data = data["users"][0]
        if student_key in student_data:
            del student_data[student_key]
            save_database(data)
            st.success("Student successfully deleted from the database!")
        else:
            st.error("Please, enter a correct Key!")

def view_all_students():
    st.subheader("All Students")
    data = load_database()
    student_data = data["users"][0]
    
    # Prepare data for table
    table_data = []
    for key, info in student_data.items():
        table_data.append({
            "Roll Number": info["rollNumber"],
            "Name": info["username"].capitalize(),
            "Email": info["email"]
        })
    
    # Display table
    st.table(table_data)


if __name__ == "__main__":
    main()