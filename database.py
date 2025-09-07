
from dotenv import load_dotenv
import os
from libsql_client import create_client

load_dotenv()
url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")
print(url,auth_token)
client = create_client(url, auth_token=auth_token)

client.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")

# Insert row
client.execute("INSERT INTO users(id) VALUES (10);")

# Query rows
rows = client.execute("SELECT * FROM users;")
print(rows)  # returns a list of Row objects
