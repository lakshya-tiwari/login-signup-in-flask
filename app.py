from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'this is about page'

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('your_name')
        passw = request.form.get('your_pass')
        db = sql.connect('/home/lakshya/Desktop/python/project/flask/database_file.db')
        show = db.execute('select *from user;').fetchall()
        for i in show:
            if i[0]==name:
                if i[2] == passw:
                    return render_template('afterlogin.html' ,value='welcome in my world')
                    break
                else:
                    return render_template('afterlogin.html', value='incorrect password')
                    break
        else:
            return render_template('afterlogin.html', value='user is not registerd in our database')


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        re_password = request.form.get('re_pass')
        if password==re_password:
            db = sql.connect('/home/lakshya/Desktop/python/project/flask/database_file.db')
            cmd = f"insert into user values('{name}', '{email}', '{password}')"
            db.execute(cmd)
            db.commit()
            return render_template('index.html')
            
        else:
            return render_template('afterlogin.html', value ='password in not matched')

if __name__ == '__main__':
    app.run(debug=True , port= 1122)
