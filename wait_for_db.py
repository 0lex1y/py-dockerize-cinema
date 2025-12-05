import socket
import time
import sys

DB_HOST = "db"
DB_PORT = 5432
TIMEOUT = 30

elapsed = 0
while elapsed < TIMEOUT:
    try:
        with socket.create_connection((DB_HOST, DB_PORT), timeout=1):
            print("Database is ready")
            sys.exit(0)
    except OSError:
        print("Waiting for database...")
        time.sleep(1)
        elapsed += 1

print("Database not ready after timeout")
sys.exit(1)
