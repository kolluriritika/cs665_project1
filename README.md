# 📚 Library Management System

## 👩‍💻 Project Overview

This is a GUI-based Library Management System built using **Python (Tkinter)** and **MySQL**. It allows users to:
- Add, view, and delete books
- Perform JOIN operations between tables
- See a structured Treeview of book data

## 🔧 Features

- Add, view, and manage Books and Members
- Predefined SQL JOIN: List Books with Author Names
- GUI built with Tkinter
- Database initialized with `create.sql` and `insert.sql`
- Delete a book with a confirmation popup
- Scrollable book list for easier navigation

## 🛠️ Tech Stack

- Python 3
- Tkinter(GUI)
- MySQL(Database)
- MySQL Connector for Python
- GitHub(Version control)

## 🗃️ Database Description

The backend uses a **MySQL relational database** named `library_db`. It contains the following tables:
1. **Authors** – Author details like name, country, and birth year
2. **Books** – Book info including title, genre, author, and ISBN
3. **Members** – Library users
4. **BorrowingHistory** – Tracks borrowing activity

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/kolluriritika/cs665_project1_library_management_system.git
    cd library_management_system
    ```

2. Run the application:
    ```bash
    python app.py
    ```

## 👤 Author

**Ritika** - Student
