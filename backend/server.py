from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymysql

app = Flask(__name__)

# MySQL connection details
hostname = 'localhost'
user = 'root'
password = '416G@*zy8k4r12'
database = 'sakila'

@app.route("/sakila")
def sakila():
    try:
        # Establish a connection to MySQL
        connection = pymysql.connect(host=hostname, user=user, password=password, database=database)

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute SQL query to fetch tables in the sakila database
        cursor.execute("SHOW TABLES")

        # Fetch all tables from the cursor
        tables = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        connection.close()

        # Convert tables tuple to list
        table_list = [table[0] for table in tables]

        # Return tables list as JSON
        return jsonify({"tables": table_list})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
