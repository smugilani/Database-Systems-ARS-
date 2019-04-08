from flask import Flask, render_template, request
#import MySQLdb
#import pymysql
#import yaml

import pymysql
myConnection = pymysql.connect(host='localhost', user='root', passwd='root', db='demo_testing_mysql')


def doQuery(conn) :
    cur = conn.cursor()

    cur.execute("SELECT username, email, gender FROM users")

    for firstname, lastname, gender in cur.fetchall():
        print('%s, %s, %s', firstname, lastname, gender)


app = Flask(__name__)

# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

#mysql = MySQLdb(app)
#mysqll = pymysql(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        cur = myConnection.cursor()
        userDetails = request.form
        firstname = userDetails['firstname']
        lastname = userDetails['lastname']
        gender = userDetails['gender']
        # cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, email, gender) VALUES(%s, %s, %s)", (firstname, lastname, gender))
        cur.connection.commit()
        # mysql.connection.commit()
        cur.close()
        #doQuery(myConnection)
        # myConnection.close()
        return 'success'
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)