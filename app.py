from flask import Flask, render_template, redirect, url_for, json, session, request
from model.LLM import *
from model.RAG import *

app = Flask(__name__, template_folder='./view')
app.secret_key = 'secret key'


@app.route('/')
def home():
    return redirect(url_for('intro'))

@app.route('/intro', methods=['GET', 'POST'])
def intro():
    click = request.form.get('click')
    if request.method == 'POST':
        if click == 'service':
            return redirect(url_for('service'))
        elif click == 'log in':
            return redirect(url_for('login'))
        elif click == 'sign up':
            return redirect(url_for('signup'))
        elif click == 'about':
            return redirect(url_for('about'))
        elif click == 'contact':
            return redirect(url_for('contact'))
    return render_template('intro.html')

@app.route('/service', methods=['GET', 'POST'])
def service():
    # if
    return render_template('service.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == ''
    return render_template('login.html')  

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    return render_template('courses.html')  

if __name__ == '__main__':
    app.run(debug=True)