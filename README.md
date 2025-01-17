# Student Management System

This is a simple Student Management System built with Streamlit. The system allows an admin to manage student data including adding, editing, deleting, and viewing student records.

## Features

- **Admin Login**: Only an admin can access the system using a predefined username and password.
- **Add Student**: Admin can add new students by providing their username and email.
- **Edit Student**: Admin can edit the details of existing students.
- **Delete Student**: Admin can delete students from the system.
- **View All Students**: Admin can view a list of all students along with their details.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/im-yjoshua/student-managment-system.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```bash
    streamlit run main_streamlit_app.py
    ```

## Usage

1. **Admin Login**: 
   - Username: `josh`
   - Password: `secret`

2. **Main Menu**: After logging in, you can choose to add, edit, delete, or view students.

3. **Add Student**: Enter the student's username and email to add a new student.

4. **Edit Student**: Enter the key of the student you want to edit, then update the username and email.

5. **Delete Student**: Enter the key of the student you want to delete from the database.

6. **View All Students**: View the list of all students currently in the database.

## File Structure

- `main_streamlit_app.py`: The main Streamlit app.
- `database/data.json`: The JSON file where student data is stored.
- `requirements.txt`: List of dependencies required for the project.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.

## Acknowledgements

Special thanks to the Streamlit team for their awesome framework!
# student-managment-system
