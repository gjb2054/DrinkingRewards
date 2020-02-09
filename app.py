from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'workout bros'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/MyProfile')
def my_profile():
    return render_template('profile.html')


@app.route('/tips', methods=['GET', 'POST'])
def tips():
    return render_template('tips.html')


@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    return render_template('workouts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        session['user'] = username

        return redirect(url_for('home'))
    return render_template("login.html")


@app.route('/signout', methods=['GET', 'POST'])
def sign_out():
    if request.method == 'POST':
        if 'user' in session:
            session.pop('user')

        return redirect(url_for("home"))
    return render_template("signout.html")

if __name__ == '__main__':
    app.run()
