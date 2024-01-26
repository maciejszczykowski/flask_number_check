from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
app.static_folder = 'static'

# PostgreSQL database configuration
db_params = {
    'database': 'Lottery_DB',
    'user': 'postgres',
    'password': 'Norw1ch!po',
    'host': 'localhost',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = request.form['number']
        result = check_number_in_db(number)
    return render_template('index.html', result=result)

def check_number_in_db(number):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    # Query the database to check if the number exists
    cursor.execute("SELECT * FROM numbers WHERE number = %s", (number,))
    
    if cursor.fetchone():
        result = "Congratulations! You win!"
    else:
        result = "Sorry, not this time"
    
    conn.close()
    return result

# Explicitly set the host to 0.0.0.0 for Docker compatibility
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
