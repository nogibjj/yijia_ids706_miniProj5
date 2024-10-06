import sqlite3

# Define a global variable for the log file
LOG_FILE = "operations_log.txt"

# Log each operation to the file
def log_operation(operation, detail=""):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{operation}: {detail}\n")

# CREATE operation - Insert data into the database
def create_CRUD(database, data):
    """Insert data into the WeatherDB table"""
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute(
        """
        INSERT INTO WeatherDB (Date, Temperature_Minimum, Temperature_Maximum, Precipitation, Snowfall, Snow_Depth, Average_Wind_Speed) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, 
        data
    )
    
    conn.commit()

    # Log the operation
    log_operation("CREATE", f"Inserted data for Date {data[0]}")
    
    conn.close()


# READ operation - Retrieve data for a specific date from the database
def read_CRUD(database, specific_date):
    """Query data from the WeatherDB table for a specific date"""
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Query data from the database for a specific date
    cursor.execute("""
        SELECT * FROM WeatherDB 
        WHERE Date = ?
    """, (specific_date,))
    results = cursor.fetchall()

    conn.close()

    # Log the operation
    log_operation("READ", f"Read records from WeatherDB for Date: {specific_date}")

    return results


# UPDATE operation - Update data in the database
def update_CRUD(database, date, new_data):
    """Update a record in the WeatherDB table based on the Date"""
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Update data based on the Date
    cursor.execute(
        """
        UPDATE WeatherDB 
        SET Temperature_Minimum=?, Temperature_Maximum=?, Precipitation=?, Snowfall=?, Snow_Depth=?, Average_Wind_Speed=? 
        WHERE Date=?
        """, 
        (*new_data, date)
    )

    conn.commit()

    # Log the operation
    log_operation("UPDATE", f"Updated data for Date {date}")

    conn.close()

# DELETE operation - Delete data from the database
def delete_CRUD(database, date):
    """Delete a record from the WeatherDB table based on the Date"""
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Delete data based on the Date
    cursor.execute("DELETE FROM WeatherDB WHERE Date=?", (date,))

    conn.commit()

    # Log the operation
    log_operation("DELETE", f"Deleted record for Date {date}")

    conn.close()
