# test_connection.py
import pytest
import psycopg2
from connection import get_connection


def test_connection():
    try:
        conn = get_connection()
        assert conn is not None
        # Check if the connection is open
        assert conn.closed == 0
        conn.close()
    except psycopg2.OperationalError as e:
        pytest.fail(f"Connection failed: {e}")
