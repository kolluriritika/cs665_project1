-- crud.sql
-- Performing CRUD operations

-- Read: Select all Members
SELECT * FROM Members;

-- Create: Add a new member
INSERT INTO Members (MemberID, Name, Email, Phone, JoinDate) VALUES
(3, 'Charlie Brown', 'charlie@example.com', '555-123-4567', '2024-03-22');

-- Update: Modify a member's phone number
UPDATE Members SET Phone = '555-987-6543' WHERE MemberID = 3;

-- Delete: Remove a Member by ID
DELETE FROM Members WHERE MemberID = 3;
