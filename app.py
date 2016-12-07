# from flask import Flask (Step 1)
from flask import Flask, render_template # (Step 2)
app = Flask(__name__)

@app.route("/")
def main():
    # return "Welcome!" (Step 1)
    return render_template('index.html') # (Step 2)

@app.route('/showSignUp') # adds signup page to routes (Step 3)
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()
