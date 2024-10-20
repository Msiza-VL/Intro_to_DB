-- Use the alx_book_store database
USE alx_book_store;

-- Query to get the full description of the books table
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
    EXTRA
FROM 
    information_schema.coslumns 
WHERE 
    table_schema = 'alx_book_store' AND 
    table_name = 'Books';
