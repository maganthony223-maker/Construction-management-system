# Construction Management System

A Django web application that helps a construction company keep organised records of its clients, employees, departments, projects, suppliers, materials, payments and project assignments. Users can add, view, update and delete records in every section.

## Group Members

| No. | Name | Registration Number |
|-----|------|---------------------|
| 1 | Hamna Muwendo | 224-063012-28127 |
| 2 | Bassi Mark | 225-063012-37887 |
| 3 | Namuli Nusufa | 425-063011-24958 |
| 4 | Nakanyago Faima | 124-063011-34677 |

## Features

- User sign up, login and logout (every page needs a login)
- Client management
- Employee and department records
- Project management with budgets and progress
- Supplier and construction material tracking
- Payment records
- Employee project assignments

## Technologies Used

- Python and Django
- SQLite database
- HTML and CSS
- Hosted on Render

## How to Run Locally

1. Clone the repository:

   ```
   git clone https://github.com/maganthony223-maker/Construction-management-system.git
   cd Construction-management-system
   ```

2. Install the requirements:

   ```
   pip install -r requirements.txt
   ```

3. Apply the database migrations:

   ```
   python manage.py migrate
   ```

4. Start the server:

   ```
   python manage.py runserver
   ```

5. Open `http://127.0.0.1:8000/` in your browser.
