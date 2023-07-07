# type: ignore
import psycopg2

TABLE_NAME = "iths.articles"


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


def create_articles_table():
    connection, cursor = create_connection()

    # Execute SQL queries to create a table
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS "{TABLE_NAME}" (
            id SERIAL PRIMARY KEY,
            title TEXT,
            description TEXT,
            link TEXT,
            published DATE,
            blog_text TEXT
        )
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


def delete_articles_table():
    connection, cursor = create_connection()

    # Execute SQL query to drop the table
    drop_table_query = f'DROP TABLE IF EXISTS "{TABLE_NAME}"'
    cursor.execute(drop_table_query)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


def add_article(articles):
    connection, cursor = create_connection()

    # Execute SQL query to insert the article into the table
    insert_query = f"""
        INSERT INTO  "{TABLE_NAME}" (title, description, link, published, blog_text)
        VALUES (%s, %s, %s, %s, %s)
    """
    for article in articles:
        cursor.execute(
            insert_query,
            (
                article.title,
                article.description,
                article.link,
                article.published,
                article.blog_text,
            ),
        )
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


def print_first_rows():
    connection, cursor = create_connection()

    # Execute the query to fetch the first 10 rows from iths.articles
    cursor.execute('SELECT * FROM "iths.articles" LIMIT 3')

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
    # delete_articles_table()
    check_tables()
    print_first_rows()
    print_column_information()
