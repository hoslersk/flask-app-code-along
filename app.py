# from flask import Flask (Step 1)
# from flask import Flask, render_template # (Step 2)
# from flask import Flask, render_template, request # adding to enable view of posted values (Step 5)
from flask import Flask, render_template, json, request # adding for json use
from flask.ext.mysql import MySQL # adding for mySQL use (Step 7)
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL() # (Step 7)

# MySQL configurations (Step 7)
app.config['MYSQL_DATABASE_USER'] = 'root'

app.config['MYSQL_DATABASE_PASSWORD'] = '' # Update for testing

app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    # return "Welcome!" (Step 1)
    return render_template('index.html') # (Step 2)

@app.route('/showSignUp') # adds signup page to routes (Step 3)
def showSignUp():
    return render_template('signup.html')

# @app.route('/signUp') # adding route for signup (Step 4)
@app.route('/signUp', methods=['POST']) # adding method for jQuery and AJAX usage (Step 5)
def signUp():
    # read the posted values from the UI (Step 6)
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values (Step 6)
    if _name and _email and _password:
        # return json.dumps({'html':'<span>All fields good !!</span>'}) # from earlier step/testing

        # below added to enable POST to mySQL w/ confirmation (Step 8)
        conn = mysql.connect()
        cursor = conn.cursor()
        _hashed_password = generate_password_hash(_password)

        cursor.callproc('sp_createUser',(_name,_email,_hashed_password))

        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            json.dumps({'message':'User created successfully !'})
        else:
            json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()
