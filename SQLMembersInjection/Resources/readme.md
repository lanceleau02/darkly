# SQL Injection

1. Go on the "Members" page.
2. Display all the users using `1 or 1=1`.
3. Display the names of tables and columns in the database using `1 or 1=1 UNION select table_name, column_name FROM information_schema.columns`.
4. Retrieve values from the `Commentaire` and `countersign` columns of the `users` table using `1 UNION SELECT Commentaire, countersign from users`.
5. Decrypt the password using MD5, lower all the characters and then encrypt it in SHA-256.