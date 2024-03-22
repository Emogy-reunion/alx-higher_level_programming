# Object Relational Mappers
## Overview
* This project is divided into two halves: the first half involves using MySQLDB for database operations, while the second half utilizes SQLAlchemy.
* MySQLDB is a lightweight library for interacting with MySQL databases using traditional SQL queries and cursor-based operations
* SQLAlchemy is a comprehensive toolkit for working with relational databases in Python, offering features such as ORM, SQL expression language, and database agnosticism
* Depending on your project requirements and preferences, you can choose the library that best fits your needs.

## MySQLDB
* MySQLDB is a Python library that provides an interface for connecting to MySQL databases using the traditional Python Database API (DB-API) interface.
* It allows Python programs to interact with MySQL databases by providing functions for executing SQL queries, fetching results, and managing database connections.

### Key features
1. Database Connection: MySQLDB allows you to establish connections to MySQL databases by providing the necessary connection parameters such as host, username, password, and database name.
2. Cursor: MySQLDB uses a cursor object to execute SQL queries and traverse the result sets. Cursors enable you to fetch data row by row and perform database operations efficiently.
3. Traditional API: MySQLDB follows the Python Database API specification, making it compatible with other database libraries that adhere to the same standard. This allows for easy integration with existing Python database codebases.

## SQLAlchemy
* SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a high-level interface for working with relational databases, allowing developers to interact with databases using Python objects instead of raw SQL queries.

### Key features
1. ORM (Object-Relational Mapping): SQLAlchemy's ORM allows you to define database models as Python classes, where each class represents a table in the database.
* This abstraction simplifies database interactions by treating database rows as objects and providing an intuitive way to query and manipulate data.
2. Database Agnostic: SQLAlchemy supports multiple database engines, including MySQL, PostgreSQL, SQLite, and more.
* This allows you to write database code that is independent of the underlying database engine, making it easier to switch between databases without modifying your application code
3. SQL Expression Language: In addition to the ORM, SQLAlchemy provides a SQL expression language that allows you to construct SQL queries using Pythonic syntax.
* This gives you full control over the generated SQL queries while still benefiting from SQLAlchemy's powerful features like automatic parameter binding and query construction.
