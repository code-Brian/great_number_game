from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
app.secret_key = 'shh'

@app.route('/')
def index():
    if('guess' not in session):
        session['guess'] = 0
    else: 
        print(f" The guess input was: {session['guess']}")

    if('rand_num' not in session):
        print('rand int generating....')
        session['rand_num'] = randint(1,100)
        print(session['rand_num'])
    
    if('message' not in session):
        session['message'] = "Guess a number!"

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print('hey, you guessed something!')
    # put code here to submit a guess 
    session['guess'] = int(request.form['guess'])

    if(session['guess'] < session['rand_num']):
        session['message'] = "Too low"
        return redirect('/')

    elif(session['guess'] > session['rand_num']):
        session['message'] = "Too high"
        return redirect('/')

    else: 
        session['message'] = "Yeah, yeah, but your scientists were so preoccupied with whether or not they could that they didn't stop to think if they should"
        return render_template('victory.html')

@app.route('/destroy', methods=['GET'])
def victory():
        session.clear()
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)