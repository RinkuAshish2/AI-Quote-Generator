#from flask import Flask,render_template
#app=Flask(__name__) #to consider main file

#@app.route('/',methods=['GET'])
#def home():
#    return "this is the first route"

#frontend is connected to backend
#@app.route('/index')
#def index_html():
#    return render_template('index.html')

#app.run(use_reloader = True)

#------------------------------------------------####----------------------------------------------------------------------###



#Example flask program Generate New Quote

import requests
import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, render_template,request,redirect, url_for,session
from flask_mysqldb import MySQL

load_dotenv()

API_KEY = os.getenv("NINJA_API_KEY")

#connecting to mysql database....
con = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)
cursor=con.cursor()

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

API_URL = "https://api.api-ninjas.com/v1/quotes"

headers = {
    "X-Api-Key": API_KEY
}

app = Flask(__name__)
app.secret_key = "supersecretkey123"
def generate_ai_quote():
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        quote = data[0]["quote"]
        author = data[0]["author"]
        return quote, author
    else:
        return "No quote received", "Unknown"

#here when we given the single "/" is can display default page will display if we mention any route it will display next where we can give the "/route".


@app.route("/index")
def home():
    quote, author = generate_ai_quote()
    return render_template(
        "index.html",
        quote=quote,
        author=author
    )

@app.route('/')
def homee():
    return render_template('home.html')

@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method=="POST":
        user=request.form['name']
        email=request.form['email']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        if password==confirm_password:

            cursor.execute('insert into registration (username,email,password) values (%s,%s,%s)',[user,email,password])
            con.commit()
        else:
            return "not matched"
        return "value stored"
    return render_template('registration.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute(
            "SELECT * FROM registration WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cursor.fetchone()

        if user:
            return redirect(url_for('home'))  # goes to /index
        else:
            return "Invalid Email or Password"
     
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('homee'))  # back to home page

if __name__ == "__main__":
    app.run(debug=True)