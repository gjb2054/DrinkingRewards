from flask import Flask, render_template
from user import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/MyProfile')
def my_profile():
    user = User('a', 'b', 'c','d', 'e','f').to_json()
    print(user)
    return render_template('profile.html', username="user", rating="1", experience="1",level="1",position="2")


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
