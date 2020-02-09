from flask import Flask, render_template, request, session, url_for, redirect
from user import User
from database_home import DatabaseHome
from tip_post import TipPost
from homie_post import HomiePost

app = Flask(__name__)
app.secret_key = 'workout bros'

DB = DatabaseHome()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user = session['user']
        homie_msg = request.form['message']

        homie_post = HomiePost(homie_msg, user)

        DB.add_homie_post(homie_post)

    homie_lst = DB.get_sorted_homie_post()

    return render_template('index.html', message="Welcome to Gym Homies, Homie", homieList=homie_lst)


@app.route('/MyProfile')
def my_profile():
    user = session['user']
    return render_template('profile.html', User=user)


@app.route('/tips', methods=['GET', 'POST'])
def tips():

    if request.method == 'POST':
        tip = request.form['tip']
        option = request.form['options']
        user = session['user']
        print
        tip_entry = TipPost(tip, user, [0], option)

        DB.add_tip_post(tip_entry)

    tips_lst = DB.get_all_tip_posts()
    return render_template('tips.html', tips=tips_lst)


@app.route('/workouts')
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

        return render_template('index.html', message="You signed in as: ", username=username)
    return render_template("login.html")


@app.route('/signout', methods=['GET', 'POST'])
def sign_out():
    if request.method == 'POST':
        if 'user' in session:
            session.pop('user')
        else:
            return render_template("index.html", message="You were not signed in!")

        return render_template("index.html", message="You signed out!")
    return render_template("signout.html")


if __name__ == '__main__':
    app.run()
