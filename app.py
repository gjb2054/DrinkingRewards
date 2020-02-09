from flask import Flask, render_template
from user import User
from database_home import DatabaseHome
from homie_post import HomiePost

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/MyProfile')
def my_profile():
    databaseHome = DatabaseHome()
    user = User('a', 'b', [5,4,3], 'd', 'e', 'f')
    databaseHome.add_user(user)
    homiePost = HomiePost("hello", user.username)
    databaseHome.add_homie_post(homiePost)
    return render_template('profile.html', User=user)


@app.route('/tips')
def tips():
    return render_template('tips.html')


@app.route('/workouts')
def workouts():
    return render_template('workouts.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
