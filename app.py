from flask import Flask, render_template
import mariadb
import dotenv
import os

app = Flask(__name__)

dotenv.load_dotenv()

DB_CONFIG = {
	'host': os.getenv('DB_HOST'),
	'user': os.getenv('DB_ADMIN_USER'),
	'password': os.getenv('DB_ADMIN_USER_PASSWORD'),
	'database': os.getenv('DB_DATABASE')
}



@app.route('/')
def initialize():
	return "Flask application"

if __name__ == '__main__':
	app.run(debug=True)