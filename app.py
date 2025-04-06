import tkinter as tk
from tkinter import ttk, messagebox
from db_connect import connect_db  # Ensure this connects to your MySQL DB

# Function to fetch books from the database
def fetch_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    records = cursor.fetchall()
    conn.close()

    # Clear Treeview
    book_list.delete(*book_list.get_children())
    for record in records:
        book_list.insert("", tk.END, values=record)

# Function to add a new book
def add_book():
    title = title_var.get()
    genre = genre_var.get()
    author_id = author_id_var.get()
    isbn = isbn_var.get()

    if not title or not genre or not author_id or not isbn:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        author_id_int = int(author_id)
    except ValueError:
        messagebox.showerror("Error", "Author ID must be a number.")
        return

    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO Books (Title, Genre, AuthorID, ISBN) VALUES (%s, %s, %s, %s)"
    values = (title, genre, author_id_int, isbn)

    try:
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Book Added Successfully!")
        fetch_books()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add book: {str(e)}")
    finally:
        conn.close()

# Function to delete a selected book
def delete_book():
    selected_item = book_list.selection()

    if not selected_item:
        messagebox.showerror("Error", "Please select a book to delete.")
        return

    # Confirm deletion
    confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this book?")
    if confirmation:
        book_id = book_list.item(selected_item)["values"][0]

        conn = connect_db()
        cursor = conn.cursor()
        query = "DELETE FROM Books WHERE BookID = %s"
        
        try:
            cursor.execute(query, (book_id,))
            conn.commit()
            messagebox.showinfo("Success", "Book Deleted Successfully!")
            fetch_books()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete book: {str(e)}")
        finally:
            conn.close()

# Function to show books and author names
def show_joins():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT Books.BookID, Books.Title, Authors.Name 
        FROM Books 
        JOIN Authors ON Books.AuthorID = Authors.AuthorID
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    book_list.delete(*book_list.get_children())
    for record in records:
        book_list.insert("", tk.END, values=record)

# UI Setup
app = tk.Tk()
app.title("📚 Library Management System")
app.geometry("800x500")
app.configure(bg="#2E4053")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12, "bold"), padding=5, background="#D5D8DC", foreground="black")
style.configure("Treeview", font=("Arial", 11), background="#ECF0F1", foreground="black", rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#3498DB", foreground="white")

# Title Label
tk.Label(app, text="Library Management System", font=("Arial", 18, "bold"), bg="#2E4053", fg="white").pack(pady=10)

# Input Frame
input_frame = tk.Frame(app, bg="#2E4053")
input_frame.pack(pady=5)

# Input Fields
title_var = tk.StringVar()
genre_var = tk.StringVar()
author_id_var = tk.StringVar()
isbn_var = tk.StringVar()

fields = [("Title", title_var), ("Genre", genre_var), ("Author ID", author_id_var), ("ISBN", isbn_var)]
for idx, (label, var) in enumerate(fields):
    tk.Label(input_frame, text=label, font=("Arial", 12, "bold"), bg="#2E4053", fg="white").grid(row=idx, column=0, padx=5, pady=3, sticky="w")
    tk.Entry(input_frame, textvariable=var, width=30, font=("Arial", 11)).grid(row=idx, column=1, padx=5, pady=3)

# Button Frame
button_frame = tk.Frame(app, bg="#2E4053")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="➕ Add Book", command=add_book).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="📚 Fetch Books", command=fetch_books).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(button_frame, text="🔍 Show Joins", command=show_joins).grid(row=0, column=2, padx=10, pady=5)
ttk.Button(button_frame, text="🗑️ Delete Book", command=delete_book).grid(row=0, column=3, padx=10, pady=5)

# Treeview for Books
tree_frame = tk.Frame(app, bg="#2E4053")
tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns = ("BookID", "Title", "Genre", "AuthorID", "ISBN")
book_list = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)

for col in columns:
    book_list.heading(col, text=col)
    book_list.column(col, anchor="center")

book_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=book_list.yview)
book_list.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the app
app.mainloop()
