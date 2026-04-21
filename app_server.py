from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Issue 1: Hardcoded secret (Security)
ADMIN_TOKEN = "SUPER_SECRET_12345"

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    # Issue 2: Mock SQL Injection vulnerability (Security)
    # Using f-strings in SQL queries is a classic vulnerability detected by static analysis
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return f"Executing query: {query}"

@app.route("/")
def index():
    # Issue 3: Unused variable (Code Style)
    unused_variable = 42
    return "Welcome to the Python Security Audit Demo"

if __name__ == "__main__":
    # Issue 4: Debug mode enabled (Security Risk)
    app.run(debug=True)
