# type: ignore
import psycopg2


def create_connection():
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="airflow",
        user="airflow",
        password="airflow",
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    return connection, cursor


def main() -> None:
    connection, cursor = create_connection()

    # Execute SQL queries to create a table
    table_name = "iths.articles"
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            content TEXT
        )
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Insert example data into the table
    insert_data_query = f"""
        INSERT INTO "{table_name}" (title)
        VALUES ('John'), ('Jane'), ('Alice')
    """
    cursor.execute(insert_data_query)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


def check_tables():
    connection, cursor = create_connection()

    # Execute the query to get a list of tables starting with 'iths.'
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'iths.%'"
    )

    # Fetch all the table names
    tables = cursor.fetchall()

    # Print the table names
    for table in tables:
        print(table[0])

    # Close the cursor and connection
    cursor.close()
    connection.close()


def print_first_10_rows():
    connection, cursor = create_connection()

    # Execute the query to fetch the first 10 rows from iths.articles
    cursor.execute('SELECT * FROM "iths.articles" LIMIT 10')

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()


def print_column_information():
    connection, cursor = create_connection()

    # Execute the query to get the column information of iths.articles
    cursor.execute(
        "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'iths.articles'"
    )

    # Fetch all the column information
    column_info = cursor.fetchall()

    # Print the column information
    for column in column_info:
        print("Column Name:", column[0])
        print("Data Type:", column[1])
        print("")

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
    check_tables()
    print_first_10_rows()
    print_column_information()
