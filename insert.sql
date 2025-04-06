-- insert.sql
-- Inserting sample data into the tables

INSERT INTO Authors (AuthorID, Name, BirthYear, Country) VALUES
(1, 'J.K. Rowling', 1965, 'United Kingdom'),
(2, 'George Orwell', 1903, 'United Kingdom'),
(3, 'Jane Austen', 1775, 'United Kingdom');

INSERT INTO Books (BookID, Title, Genre, AuthorID, ISBN) VALUES
(1, 'Harry Potter and the Sorcerer\'s Stone', 'Fantasy', 1, '978-0439708180'),
(2, '1984', 'Dystopian', 2, '978-0451524935'),
(3, 'Pride and Prejudice', 'Romance', 3, '978-1503290563');


INSERT INTO Members (MemberID, Name, Email, Phone, JoinDate) VALUES
(1, 'Alice Johnson', 'alice@example.com', '123-456-7890', '2023-06-15'),
(2, 'Bob Smith', 'bob@example.com', '987-654-3210', '2024-01-20');

INSERT INTO BorrowingHistory (BorrowID, MemberID, BookID, BorrowDate, ReturnDate) VALUES
(1, 1, 1, '2024-03-01', '2024-03-15'),
(2, 2, 2, '2024-03-05', NULL);

