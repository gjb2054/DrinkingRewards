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
    databaseHome = DatabaseHome()
    user = User('a', 'b', [5,4,3], 'd', 'e', 'f')
    databaseHome.add_user(user)
    homiePost = HomiePost("hello", user.username)
    databaseHome.add_homie_post(homiePost)
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

    tips_weight = DB.get_spec_tips("weight lifting")
    tips_cardio = DB.get_spec_tips("Cardio")
    tips_call = DB.get_spec_tips("Callisthenics")
    tips_body = DB.get_spec_tips("Body Builder")

    return render_template('tips.html', t_weights=tips_weight, t_cardio=tips_cardio, t_call=tips_call, t_body=tips_body)


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
