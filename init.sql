-- Drop existing table if it exists
DROP TABLE IF EXISTS users;

-- Create the users table with an added phone field
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15)  -- Added phone field
);

