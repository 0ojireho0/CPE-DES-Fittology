from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask('__name__')
app.secret_key = 'your-secret-key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session.get('username'))
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT username, fullname, password FROM tbl_users WHERE username = '{username}' ")
        user = cur.fetchone()
        cur.close()
        if user and pwd == user[2]:  # assuming password is the third column
            session['username'] = user[0]
            session['fullname'] = user[1]  # storing full name in session
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        fullname = request.form['fullname']
        pwd = request.form['password']
        injuries = request.form['injuries']
        injuries2 = request.form['injuries2']
        
        # Check if either injuries or injuries2 is set to "yes"
        if injuries == "yes" or injuries2 == "yes":
            # If yes, return some message or redirect back to the registration page
            return render_template('register.html', not_allowed="Sorry, registration not allowed for users with injuries")
        
        # If neither injuries nor injuries2 is set to "yes", proceed with registration
        cur = mysql.connection.cursor()
        cur.execute(f"insert into tbl_users (username, password, fullname) values ('{username}', '{pwd}', '{fullname}')")
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)
