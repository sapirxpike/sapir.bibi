from flask import Flask , redirect , url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'WELCOME TO FACEBOOK!  :   https://www.cinema-city.co.il/   -   http://saillavie.co.il/'

@app.route('/about1')
def about1_func():
    return " welcome to about1 page"


@app.route('/catalog1')
def catalog1_func():
    return redirect(url_for('about1_func'))


if __name__ == '__main__':
    app.run(debug=True)
