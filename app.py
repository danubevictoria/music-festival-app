import csv
from flask import Flask, url_for, render_template, json, request, Response
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from test.test_userstring import UserStringTest

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'J3taime2'
app.config['MYSQL_DATABASE_DB'] = 'MusicApp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def api_root():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/usersignup')
def showSignUp():
    return render_template('signup.html')

@app.route('/signup',methods=['POST', 'GET'])
def signUp():
    try:
        # read the posted values from the UI
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        
        # validate the received values
        if _name and _email and _password:
        # All Good, let's call MySQL
                
                conn = mysql.connect()
                cursor = conn.cursor()
                '''_hashed_password = generate_password_hash(_password)'''
                cursor.callproc('sp_createUser',(_name,_email,_password))
                data = cursor.fetchall()
    
                if len(data) is 0:
                    conn.commit()
                    return json.dumps({'message':'User created successfully !'})
                else:
                    return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
        cursor.close() 
        conn.close()
    except Exception as e:
        return json.dumps(str(e))
    
@app.route('/usersignin')
def showSignIn():
    return render_template('signin.html')

@app.route('/signin',methods=['GET', 'POST'])
def signIn():
    try:
        _myusername = request.form['signinEmail']
        _mypassword = request.form['signinPassword']
    
        if _myusername and _mypassword:
            # All Good, let's call MySQL
                    
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT user_id FROM Users WHERE user_username ='" + _myusername + "' and user_password = '" + _mypassword + "'")
            data = cursor.fetchall()
        
            if len(data) is 1:
                conn.commit()
                return json.dumps({'message':'Logged in successfully !'})
            else:
                return json.dumps({'error':'Incorrect password or username. Or user does not exist.'})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
        cursor.close() 
        conn.close()
    except Exception as e:
        return json.dumps(str(e))
    
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
'''
@app.route('/upload', methods=['GET', 'POST'])
def upload:
    try:
        _fileToUpload = request.form['fileToUpload']
        
        if _fileToUpload:
            csv_data = csv.reader(file('_fileToUpload'))
            for row in csv_data:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute('INSERT INTO testcsv(names, \
                      classes, mark )' \
                      'VALUES("%s", "%s", "%s")',
                      row)
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
        mysql.commit()
        cursor.close() 
        conn.close()
        print "Done"
    except Exception as e:
        return json.dumps(str(e))
 '''   
@app.route('/thankyou')
def thankYou():
    return render_template('thankyou.html')
    
@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/error')
def error():
    return render_template('404.html')

if __name__ == '__main__':
    app.run()
