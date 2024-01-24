# Welcome to In-Memory-Database Python program

This Python program is implement an in-memory database interaction using a CLI or command-line interface.
TThis Python program reads an STDIN line by line, that can execute various database functions.

Here is an overview of the supported commands:
SET [name] [value]: Sets the value associated with the given name in the database.
GET [name]: Retrieves and prints the value for the specified name. If the name is not in the database, print "NULL."
DELETE [name]: Deletes the value associated with the specified name from the database.
COUNT [value]: Returns the count of names that have the given value assigned to them. If the value is not assigned to any name, print "0."
BEGIN: Starts a new transaction.
ROLLBACK: Rolls back the most recent transaction. If there is no transaction to rollback, print "TRANSACTION NOT FOUND."
COMMIT: Commits all open transactions and makes changes permanent.
END: Exits the database.
 
**1. Local Setup Instructions:**
	Using Visual Studio Code, follow these steps:
		Install Python on your system with a supported version _(Used version in the demo: Python 3.11)_ **(Note: Using macOS is not supported in this demo)**
		Make sure to install also the Python extension 
		Select **Python Interpreter** from the Status Bar
		Open Terminal and Run the Python script using Python.exe, for example:

	& C:/python.exe C:/inmemorydatabase.py

2. Sample test case here. Input the following lines with expected output in **bold characters**:

GET a
Output: NULL

SET a foo
Output: SET a => foo

SET b foo
Output: SET b => foo

COUNT foo
Output: COUNT foo => 2

COUNT bar
Output: COUNT bar => 0

DELETE a
Output: DELETE a

COUNT foo
Output: COUNT foo => 1

SET b baz
Output: SET b => baz

COUNT foo
Output: COUNT foo => 0

GET b
Output: GET b => baz

GET B
Output: GET B => NULL

END
Output: END

The provided commands demonstrate basic usage of the in-memory database functionality.
Feel free to explore and experiment with additional commands as needed.






