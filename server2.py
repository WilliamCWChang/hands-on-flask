#!flask/bin/python
from flask import Flask, jsonify, url_for, render_template
from flask import request


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/echoooooo')
def echoooooo():
    return 'echoooooo, World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    return "do_the_login"


def show_the_login_form():
    return "show_the_login_form"


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


@app.route('/api_test', methods=['PUT', 'GET'])
def api_test():
    error = None
    if request.method == 'PUT':
        data = [request.form['username'], request.form['password']]
        return str(data)
    elif request.method == 'GET':
        return "HELLO"

    return render_template('api_test.html', error=error)


if __name__ == '__main__':
    control = 0

    if control == 0:
        app.run(debug=True)
    elif control == 1:
        with app.test_request_context():
            print(url_for('index'))
            print(url_for('login'))
            print(url_for('login', next='/'))
            print(url_for('profile', username='John Doe'))
    else:
        raise AssertionError("do not have this control")
