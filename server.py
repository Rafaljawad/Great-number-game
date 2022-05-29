
from flask import Flask,request,redirect,render_template,session
import random

app=Flask(__name__)
app.secret_key = ' keep it safe'


@app.route('/')
def show():
    if 'counter' not in session:
        session['counter']=0
    if 'random' not in session:
        session['random']= random.randint(1, 100)
    if 'number' not in session:
        session['number']=0
    return render_template('index.html')
# Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
@app.route('/guess',methods=['POST'])
def choose_num():
    session['counter']+=1;
    session['number']=int(request.form['number'])
    return redirect('/')
@app.route('/again')
def clear():
    session.clear()
    return redirect('/')

@app.route('/congrats',methods=['POST'])
def congrats_message():
    session['name']=request.form['name']
    return render_template('index2.html')


@app.route('/back')
def back_to_main():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)