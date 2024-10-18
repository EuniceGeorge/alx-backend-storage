-- creates a table users following these requirements
ALTER TABLE users
ADD COLUMN country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US';
