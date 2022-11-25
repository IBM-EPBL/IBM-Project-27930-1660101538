from flask import Flask, render_template 

app = Flask(__name__) 

@app.route("/signin")

def sign_in():
    return render_template("shoping.html")
@app.route('/signup')
def sign_up():
    return render_template("login.html")
@app.route('/')
def home():
    return render_template("shoping.html")
@app.route('/about')
def about():
    return render_template("shoping.html")
if __name__ == '__main__':
    app.run(debug=True)
