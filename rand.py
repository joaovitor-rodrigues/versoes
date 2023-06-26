from flask import Flask, redirect, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['GET', 'POST'])
def button():
    redirect_page = random.choice(['um', 'dois', 'tres'])
    return redirect(redirect_page)

@app.route('/um')
def page1():
    return render_template('um.html')

@app.route('/dois')
def page2():
    return render_template('dois.html')

@app.route('/tres')
def page3():
    return render_template('tres.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
