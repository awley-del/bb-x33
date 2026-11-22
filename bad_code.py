import sqlite3, os

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def lookup_user(email):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    return conn.execute(query).fetchall()


def run(cmd):
    return os.system("convert " + cmd)
