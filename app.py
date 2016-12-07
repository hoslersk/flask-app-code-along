# from flask import Flask (Step 1)
# from flask import Flask, render_template # (Step 2)
# from flask import Flask, render_template, request # adding to enable view of posted values (Step 5)
from flask import Flask, render_template, json, request # adding for json use
app = Flask(__name__)

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
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()
