import sqlite3

# Define a global variable for the log file
LOG_FILE = "operations_log.md"

# Log each operation to the markdown file in a SQL code block format
def log_operation(operation, detail=""):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"```sql\n{operation}\n```\n\n")


# CREATE operation - Insert data into the database
def create_CRUD(database, data):
    """Insert data into the WeatherDB table"""
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Insert data into the database
    query = """
    INSERT INTO WeatherDB (Date, Temperature_Minimum, Temperature_Maximum, Precipitation, Snowfall, Snow_Depth, Average_Wind_Speed)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, data)
    
    conn.commit()

    # Log the operation in SQL format
    log_operation(query, f"Inserted data for Date {data[0]}")

    conn.close()


# READ operation - Retrieve data for a specific date from the database
def read_CRUD(database, specific_date):
    """Query data from the WeatherDB table for a specific date"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = """
    SELECT * FROM WeatherDB WHERE Date = ?
    """
    cursor.execute(query, (specific_date,))
    results = cursor.fetchall()

    conn.close()

    # Log the operation in SQL format
    log_operation(query, f"Read records from WeatherDB for Date: {specific_date}")

    return results


# UPDATE operation - Update data in the database
def update_CRUD(database, date, new_data):
    """Update a record in the WeatherDB table based on the Date"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = """
    UPDATE WeatherDB 
    SET Temperature_Minimum=?, Temperature_Maximum=?, Precipitation=?, Snowfall=?, Snow_Depth=?, Average_Wind_Speed=? 
    WHERE Date=?
    """
    cursor.execute(query, (*new_data, date))

    conn.commit()

    # Log the operation in SQL format
    log_operation(query, f"Updated data for Date {date}")

    conn.close()


# DELETE operation - Delete data from the database
def delete_CRUD(database, date):
    """Delete a record from the WeatherDB table based on the Date"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = "DELETE FROM WeatherDB WHERE Date=?"
    cursor.execute(query, (date,))

    conn.commit()

    # Log the operation in SQL format
    log_operation(query, f"Deleted record for Date {date}")

    conn.close()