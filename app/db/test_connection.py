import os
import pytest
from connection import connect, close

# Set environment variables for testing (You can replace these with your actual values)
os.environ['PASSWORD'] = '#iLoveB6##@2024'  # Replace with your actual password
os.environ['HOST'] = 'localhost'  # Replace with your actual host
os.environ['PORT'] = '5432'  # Replace with your actual port
os.environ['DBNAME'] = 'your_database_name'  # Replace with your actual database name


def test_database_connection():
    """Test the database connection."""
    connection, cursor = connect()
    assert connection is not None, "Connection should not be None"
    assert cursor is not None, "Cursor should not be None"

    # You can also run a simple query to ensure everything works
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    assert db_version is not None, "Database version should not be None"

    print(f"Database version: {db_version[0]}")

    # Close the connection after the test
    close(connection, cursor)


if __name__ == "__main__":
    pytest.main()
