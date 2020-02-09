from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/MyProfile')
def my_profile():
    return render_template('profile.html')


@app.route('/tips')
def tips():
    return render_template('tips')



if __name__ == '__main__':
    app.run()
