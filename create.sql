-- create.sql
-- Creating tables for the Library Management System

CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,  -- AuthorID -> Name, BirthYear, Country
    Name TEXT NOT NULL,
    BirthYear INTEGER,
    Country TEXT
);


CREATE TABLE Books (
    BookID INTEGER  AUTO_INCREMENT PRIMARY KEY,  -- BookID -> Title, Genre, AuthorID, ISBN
    Title TEXT NOT NULL,
    Genre TEXT,
    AuthorID INTEGER,
    ISBN VARCHAR(20) UNIQUE,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

CREATE TABLE Members (
    MemberID INTEGER PRIMARY KEY,  -- MemberID -> Name, Email, Phone, JoinDate
    Name TEXT NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    JoinDate DATE
);

CREATE TABLE BorrowingHistory (
    BorrowID INTEGER PRIMARY KEY,  -- BorrowID -> MemberID, BookID, BorrowDate, ReturnDate
    MemberID INTEGER,
    BookID INTEGER,
    BorrowDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);
