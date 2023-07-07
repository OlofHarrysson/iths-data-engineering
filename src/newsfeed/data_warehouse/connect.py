import psycopg2


def main() -> None:
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

    # Execute SQL queries to create a table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        )
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Insert example data into the table
    insert_data_query = """
        INSERT INTO example_table (name)
        VALUES ('John'), ('Jane'), ('Alice')
    """
    cursor.execute(insert_data_query)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
