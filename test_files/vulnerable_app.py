import os
import sqlite3

# VULNERABILITY 1: Hardcoded Secret
AWS_SECRET_KEY = "AKIA1234567890" 
DB_PASSWORD = "password123"

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # VULNERABILITY 2: SQL Injection
    # The user input is directly concatenated into the query string
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    
    cursor.execute(query)
    return cursor.fetchall()

def run_command(user_input):
    # VULNERABILITY 3: Command Injection
    # Executing raw system commands from user input
    os.system("echo " + user_input)

if __name__ == "__main__":
    u = input("Enter name: ")
    print(get_user_data(u))