from flask import Flask, render_template, request

app = Flask(__name__)


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
    if request.method == 'POST':


    return render_template('workouts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template()


if __name__ == '__main__':
    app.run()
