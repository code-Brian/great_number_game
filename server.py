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

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print('hey, you guessed something!')
    # put code here to submit a guess 
    session['guess'] = int(request.form['guess'])

    if(session['guess'] != session['rand_num']):
        print(f"guess again, hammy")
        print(session['guess'])
        return redirect('/')
    else: 
        print('wooohooo you did it! gj gj gj gj gj gj')
        # return redirect('/success')
    return redirect('/')

# @app.route('/success')


if __name__ == '__main__':
    app.run(debug=True)